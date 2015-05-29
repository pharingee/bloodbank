from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from forms import (
    DonationDetailsForm, DonationPreForm, DonationFormA, DonationFormB,
    DonationFormC, BloodForm, HospitalTestForm, NBTSTestForm, DonorDetailsForm
)
from models import Donor, Blood


def donate_details(request):
    form = DonationDetailsForm()
    if request.method == 'POST':
        form = DonationDetailsForm(request.POST)

        if form.is_valid():
            donor = None
            blood = None
            has_untaken_blood = False
            try:
                donor = Donor.objects.get(number=form.cleaned_data['number'])
                for blood_donated in donor.donated_blood.all():
                    if not blood_donated.is_taken:
                        blood = blood_donated
                        has_untaken_blood = True
            except Donor.DoesNotExist:
                donor = form.save()

            if not has_untaken_blood:
                blood = Blood.objects.create(
                    donor=donor, hospital=form.cleaned_data['hospital'])

            return redirect(
                reverse('donations:donate_pre_form', args=[blood.id]))

    return render(request, 'donate.html', {'form': form})


def donate_pre_form(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    try:
        form = DonationPreForm(
            request.POST or None, instance=blood.donorconditionpreform)
    except:
        form = DonationPreForm(request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            pre_form = form.save()
            today = date.today()

            if not pre_form.is_first_donation:
                if (today.year - pre_form.last_donation_date.year) < 2:
                    return redirect(
                        reverse(
                            'donations:donate_form_b',
                            args=(pre_form.blood.id,)))

            return redirect(
                reverse(
                    'donations:donate_form_a', args=(pre_form.blood.id,)))

    return render(request, 'donate.html', {'form': form})


def donate_form_a(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    try:
        form = DonationFormA(
            request.POST or None, instance=blood.donorconditionforma)
    except:
        form = DonationFormA(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form_a = form.save()

            return redirect(
                reverse(
                    'donations:donate_form_b', args=(form_a.blood.id,)))

    return render(request, 'donate.html', {'form': form})


def donate_form_b(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    try:
        form = DonationFormB(
            request.POST or None, instance=blood.donorconditionformb)
    except:
        form = DonationFormB(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():

            form_b = form.save()

            return redirect(
                reverse(
                    'donations:donate_form_c', args=(form_b.blood.id,)))

    return render(request, 'donate.html', {'form': form})


def donate_form_c(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    try:
        form = DonationFormC(
            request.POST or None, instance=blood.donorconditionformc)
    except:
        form = DonationFormC(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('donations:donate_thankyou')

    return render(request, 'donate.html', {'form': form})


def donate_thankyou(request):
    return render(request, 'thankyou.html')


@login_required
def donors(request):
    if request.user.is_nbts:
        donor_list = Donor.objects.all()
    else:
        donor_list = Donor.objects.filter(
            donated_blood__hospital=request.user.hospital)

    return render(
        request, 'dashboard/donations/donor-list.html',
        {'donor_list': donor_list})


@login_required
def donor(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    blood = None
    for blood in donor.donated_blood.all():
        if not blood.is_taken:
            blood = blood

    if not request.user.is_nbts:
        is_hospital = False
        for blood in donor.donated_blood.all():
            if blood.hospital == request.user.hospital:
                is_hospital = True

        if not is_hospital:
            return render(request, 'dashboard/donations/no-access.html')

    form = DonorDetailsForm(request.POST or None, instance=donor)
    if request.method == 'POST':

        if form.is_valid():
            donor = None
            blood = None
            has_untaken_blood = False
            try:
                donor = Donor.objects.get(number=form.cleaned_data['number'])
                donor = form.save()
                for blood_donated in donor.donated_blood.all():
                    if not blood_donated.is_taken:
                        blood = blood_donated
                        has_untaken_blood = True
            except Donor.DoesNotExist:
                donor = form.save()

            if not has_untaken_blood:
                blood = Blood.objects.create(
                    donor=donor, hospital=form.cleaned_data['hospital'])

            return redirect(
                reverse('donations:donor', args=[donor.id]))

    return render(
        request, 'dashboard/donations/donor.html',
        {'blood_id': blood.id, 'donor_id': donor.id, 'form': form})


@login_required
def donor_donations(request, donor_id):
    donor = get_object_or_404(Donor, pk=donor_id)
    donations = []
    if not request.user.is_nbts:
        is_hospital = False
        for blood in donor.donated_blood.all():
            if blood.hospital == request.user.hospital:
                is_hospital = True
                donations.append(blood)

        if not is_hospital:
            return render(request, 'dashboard/donations/no-access.html')

    return render(
        request, 'dashboard/donations/donor-donations.html',
        {'donations': donations})


@login_required
def list(request):
    if request.user.is_nbts:
        blood_list = Blood.objects.filter(is_nbts_approved=False)
    else:
        blood_list = request.user.hospital.bloods.all(is_nbts_approved=False)

    return render(
        request, 'dashboard/donations/blood-list.html',
        {'blood_list': blood_list})


@login_required
def blood(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    if not request.user.is_nbts:
        if blood.hospital != request.user.hospital:
            return render(request, 'dashboard/donations/no-access.html')

    form = BloodForm(request.POST or None, instance=blood)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect(reverse('donations:blood', args=(blood_id)))

    return render(
        request, 'dashboard/donations/blood.html',
        {'form': form, 'blood_id': blood_id, 'donor_id': blood.donor.id})


@login_required
def pre_form(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    if not request.user.is_nbts:
        if blood.hospital != request.user.hospital:
            return render(request, 'dashboard/donations/no-access.html')

    try:
        form = DonationPreForm(
            request.POST or None, instance=blood.donorconditionpreform)
    except:
        form = DonationPreForm(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect(reverse('donations:pre_form', args=(blood_id)))

    return render(
        request, 'dashboard/donations/blood.html',
        {'form': form, 'blood_id': blood_id, 'donor_id': blood.donor.id})


@login_required
def form_a(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    if not request.user.is_nbts:
        if blood.hospital != request.user.hospital:
            return render(request, 'dashboard/donations/no-access.html')

    try:
        form = DonationFormA(
            request.POST or None, instance=blood.donorconditionforma)
    except:
        form = DonationFormA(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect(reverse('donations:form_a', args=(blood_id)))

    return render(
        request, 'dashboard/donations/blood.html',
        {'form': form, 'blood_id': blood_id, 'donor_id': blood.donor.id})


@login_required
def form_b(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    if not request.user.is_nbts:
        if blood.hospital != request.user.hospital:
            return render(request, 'dashboard/donations/no-access.html')

    try:
        form = DonationFormB(
            request.POST or None, instance=blood.donorconditionformb)
    except:
        form = DonationFormB(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect(reverse('donations:form_b', args=(blood_id)))

    return render(
        request, 'dashboard/donations/blood.html',
        {'form': form, 'blood_id': blood_id, 'donor_id': blood.donor.id})


@login_required
def form_c(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    if not request.user.is_nbts:
        if blood.hospital != request.user.hospital:
            return render(request, 'dashboard/donations/no-access.html')

    try:
        form = DonationFormC(
            request.POST or None, instance=blood.donorconditionformc)
    except:
        form = DonationFormC(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect(reverse('donations:form_c', args=(blood_id)))

    return render(
        request, 'dashboard/donations/blood.html',
        {'form': form, 'blood_id': blood_id, 'donor_id': blood.donor.id})


@login_required
def hospital(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    if not request.user.is_nbts:
        if blood.hospital != request.user.hospital:
            return render(request, 'dashboard/donations/no-access.html')

    try:
        form = HospitalTestForm(
            request.POST or None, instance=blood.hospitaltest)
    except:
        form = HospitalTestForm(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect(reverse('donations:hospital', args=(blood_id)))

    return render(
        request, 'dashboard/donations/blood.html',
        {'form': form, 'blood_id': blood_id, 'donor_id': blood.donor.id})


@login_required
def nbts(request, blood_id):
    blood = get_object_or_404(Blood, pk=blood_id)
    if not request.user.is_nbts:
        return render(request, 'dashboard/donations/no-access.html')

    try:
        form = NBTSTestForm(
            request.POST or None, instance=blood.nbtstest)
    except:
        form = NBTSTestForm(
            request.POST or None, initial={'blood': blood})

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect(reverse('donations:nbts', args=(blood_id)))

    return render(
        request, 'dashboard/donations/blood.html',
        {'form': form, 'blood_id': blood_id, 'donor_id': blood.donor.id})
