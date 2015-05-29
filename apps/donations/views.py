from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from forms import (
    DonationDetailsForm, DonationPreForm, DonationFormA, DonationFormB,
    DonationFormC
)


def donate_details(request):
    form = DonationDetailsForm()
    if request.method == 'POST':
        form = DonationDetailsForm(request.POST)

        if form.is_valid():
            donor = form.save()
            redirect(
                reverse('donate_pre_form', args=(donor.donor_id,)))
    return render(request, 'donate.html', {'form': form})


def donate_pre_form(request, donor_id):
    form = DonationPreForm()
    if request.method == 'POST':
        form = DonationPreForm(request.POST)

        if form.is_valid():
            pre_form = form.save()
            redirect(
                reverse('donate_pre_form', args=(pre_form.blood.donorid,)))
    return render(request, 'donate.html', {'form': form})


def donate_form_a(request, donor_id):
    form = DonationFormA()
    if request.method == 'POST':
        form = DonationFormA(request.POST)

        if form.is_valid():
            form_a = form.save()
            redirect(
                reverse('donate_pre_form', args=(form_a.blood.donorid,)))
    return render(request, 'donate.html', {'form': form})


def donate_form_b(request, donor_id):
    form = DonationFormB()
    if request.method == 'POST':
        form = DonationFormB(request.POST)

        if form.is_valid():
            form_b = form.save()
            redirect(
                reverse('donate_pre_form', args=(form_b.blood.donorid,)))
    return render(request, 'donate.html', {'form': form})


def donate_form_c(request, donor_id):
    form = DonationFormC()
    if request.method == 'POST':
        form = DonationFormC(request.POST)

        if form.is_valid():
            form_c = form.save()
            redirect(
                reverse('donate_pre_form', args=(form_c.blood.donorid,)))
    return render(request, 'donate.html', {'form': form})
