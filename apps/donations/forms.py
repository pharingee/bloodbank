from django import forms
from django.forms.extras.widgets import SelectDateWidget
from models import (
    Donor, Blood, BloodProduct, HospitalTest, NBTSTest, DonorConditionFormA,
    DonorConditionFormB, DonorConditionFormC, DonorConditionPreForm
)


class DonationDetailsForm(forms.ModelForm):

    class Meta:
        model = Donor
        fields = ['name', 'number', 'age', 'gender' ,'blood_group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
        }


class DonationPreForm(forms.ModelForm):

    class Meta:
        model = DonorConditionPreForm
        fields = [
            'is_first_donation', 'last_donation_place', 'last_donation_date']
        widgets = {
            'last_donation_place': forms.TextInput(
                attrs={'class': 'form-control'}),
            'last_donation_date': SelectDateWidget(),
        }


class DonationFormA(forms.ModelForm):

    class Meta:
        model = DonorConditionFormA
        fields = [
            'advised_against_giving', 'anaemia', 'serious_illness',
            'neurosurgical_procedure', 'transplant', 'growth_hormone',
            'head_injury', 'blood_pressure_issue', 'bowel_disease',
            'kidney_problem', 'diabetes', 'cancer', 'malaria', 'jaundice',
            'tigason']
        widgets = {
            'advised_against_giving': forms.Select(
                attrs={'class': 'form-control'}),
            'anaemia': forms.Select(
                attrs={'class': 'form-control'}),
            'serious_illness': forms.Select(
                attrs={'class': 'form-control'}),
            'neurosurgical_procedure': forms.Select(
                attrs={'class': 'form-control'}),
            'transplant': forms.Select(
                attrs={'class': 'form-control'}),
            'growth_hormone': forms.Select(
                attrs={'class': 'form-control'}),
            'head_injury': forms.Select(
                attrs={'class': 'form-control'}),
            'blood_pressure_issue': forms.Select(
                attrs={'class': 'form-control'}),
            'bowel_disease': forms.Select(
                attrs={'class': 'form-control'}),
            'kidney_problem': forms.Select(
                attrs={'class': 'form-control'}),
            'diabetes': forms.Select(
                attrs={'class': 'form-control'}),
            'cancer': forms.Select(
                attrs={'class': 'form-control'}),
            'malaria': forms.Select(
                attrs={'class': 'form-control'}),
            'jaundice': forms.Select(
                attrs={'class': 'form-control'}),
            'tigason': forms.Select(
                attrs={'class': 'form-control'})
        }


class DonationFormB(forms.ModelForm):

    class Meta:
        model = DonorConditionFormB
        fields = [
            'feeling_healthy', 'ever_pregnant', 'pregnancy_count',
            'recent_pregnancy', 'risk_of_injury_activities', 'dental_work',
            'pain_killers', 'cuts', 'gastric_upset', 'recent_unwellness',
            'recent_chest_pain', 'recent_skin_condition', 'recent_medication',
            'recent_abattoir', 'recent_sexual_infection',
            'recent_immunizations', 'recent_chicken_pox'
        ]
        widgets = {
            'feeling_healthy': forms.Select(
                attrs={'class': 'form-control'}),
            'ever_pregnant': forms.Select(
                attrs={'class': 'form-control'}),
            'pregnancy_count': forms.NumberInput(
                attrs={'class': 'form-control'}),
            'recent_pregnancy': forms.Select(
                attrs={'class': 'form-control'}),
            'risk_of_injury_activities': forms.Select(
                attrs={'class': 'form-control'}),
            'dental_work': forms.Select(
                attrs={'class': 'form-control'}),
            'pain_killers': forms.Select(
                attrs={'class': 'form-control'}),
            'cuts': forms.Select(
                attrs={'class': 'form-control'}),
            'gastric_upset': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_unwellness': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_chest_pain': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_skin_condition': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_medication': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_abattoir': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_sexual_infection': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_immunizations': forms.Select(
                attrs={'class': 'form-control'}),
            'recent_chicken_pox': forms.Select(
                attrs={'class': 'form-control'})
        }


class DonationFormC(forms.ModelForm):

    class Meta:
        model = DonorConditionFormC


class HospitalTestForm(forms.ModelForm):

    class Meta:
        model = HospitalTest


class NBTSTestForm(forms.ModelForm):

    class Meta:
        model = NBTSTest


class BloodProductForm(forms.ModelForm):

    class Meta:
        model = BloodProduct


class BloodForm(forms.ModelForm):

    class Meta:
        model = Blood
