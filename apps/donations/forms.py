from django import forms
from django.forms.extras.widgets import SelectDateWidget
from models import (
    Donor, Blood, BloodProduct, HospitalTest, NBGSTest, DonorConditionFormA,
    DonorConditionFormB, DonorConditionFormC, DonorConditionPreForm
)
from apps.users.models import Hospital


class DonorDetailsForm(forms.ModelForm):

    class Meta:
        model = Donor
        fields = [
            'name', 'number', 'age', 'gender', 'blood_group', 'is_rh_positive'
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'number': forms.TextInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'age': forms.NumberInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'gender': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'blood_group': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'is_rh_positive': forms.Select(
                attrs={'class': 'input-xxlarge form-control'})
        }


class DonationDetailsForm(forms.ModelForm):
    hospital = forms.ModelChoiceField(
        queryset=Hospital.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Donor
        fields = ['name', 'number', 'age', 'gender']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'number': forms.TextInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'age': forms.NumberInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'gender': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
        }


class DonationPreForm(forms.ModelForm):

    class Meta:
        model = DonorConditionPreForm
        fields = [
            'is_first_donation', 'last_donation_place', 'last_donation_date',
            'blood']
        widgets = {
            'last_donation_place': forms.TextInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'last_donation_date': SelectDateWidget(
                years=[2010, 2011, 2012, 2013, 2014, 2015]),
            'is_first_donation': forms.Select(attrs={'class': 'form-control'}),
            'blood': forms.HiddenInput()
        }


class DonationFormA(forms.ModelForm):

    class Meta:
        model = DonorConditionFormA
        fields = [
            'advised_against_giving', 'anaemia', 'serious_illness',
            'transplant', 'head_injury', 'blood_pressure_issue',
            'bowel_disease', 'kidney_problem', 'diabetes', 'cancer',
            'malaria', 'jaundice', 'blood']
        widgets = {
            'advised_against_giving': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'anaemia': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'serious_illness': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'transplant': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'head_injury': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'blood_pressure_issue': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'bowel_disease': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'kidney_problem': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'diabetes': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'cancer': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'malaria': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'jaundice': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'blood': forms.HiddenInput()
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
            'recent_immunizations', 'recent_chicken_pox', 'blood'
        ]
        widgets = {
            'feeling_healthy': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'ever_pregnant': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'pregnancy_count': forms.NumberInput(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_pregnancy': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'risk_of_injury_activities': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'dental_work': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'pain_killers': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'cuts': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'gastric_upset': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_unwellness': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_chest_pain': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_skin_condition': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_medication': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_abattoir': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_sexual_infection': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_immunizations': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'recent_chicken_pox': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'blood': forms.HiddenInput()
        }


class DonationFormC(forms.ModelForm):

    class Meta:
        model = DonorConditionFormC
        fields = [
            'blood', 'aids', 'unprescibed_injection', 'clotting_factors',
            'hepatitis', 'swollen_glands', 'sex_with_above',
            'blood_transfusion', 'injured_with_needle', 'tatoo'
        ]
        widgets = {
            'blood': forms.HiddenInput(),
            'aids': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'unprescibed_injection': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'clotting_factors': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hepatitis': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'swollen_glands': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'sex_with_above': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'blood_transfusion': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'injured_with_needle': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'tatoo': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
        }


class HospitalTestForm(forms.ModelForm):

    class Meta:
        model = HospitalTest
        fields = [
            'blood', 'blood_type_crossmatch', 'adverse_antibodies',
            'infectious_agents', 'blood_group_antibodies', 'hiv1', 'hiv2',
            'htlv_I', 'htlv_II', 'hepatitis_B', 'hepatitis_C', 'syphillis',
            'west_nile', 'chagas'
        ]
        widgets = {
            'blood': forms.HiddenInput(),
            'blood_type_crossmatch': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'adverse_antibodies': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'infectious_agents': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'blood_group_antibodies': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hiv1': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hiv2': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'htlv_I': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'htlv_II': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hepatitis_B': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hepatitis_C': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'syphillis': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'west_nile': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'chagas': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
        }


class NBTSTestForm(forms.ModelForm):

    class Meta:
        model = NBGSTest
        fields = [
            'blood', 'blood_type_crossmatch', 'adverse_antibodies',
            'infectious_agents', 'blood_group_antibodies', 'hiv1', 'hiv2',
            'htlv_I', 'htlv_II', 'hepatitis_B', 'hepatitis_C', 'syphillis',
            'west_nile', 'chagas'
        ]
        widgets = {
            'blood': forms.HiddenInput(),
            'blood_type_crossmatch': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'adverse_antibodies': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'infectious_agents': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'blood_group_antibodies': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hiv1': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hiv2': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'htlv_I': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'htlv_II': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hepatitis_B': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'hepatitis_C': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'syphillis': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'west_nile': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
            'chagas': forms.Select(
                attrs={'class': 'input-xxlarge form-control'}),
        }


class BloodProductForm(forms.ModelForm):

    class Meta:
        model = BloodProduct
        fields = ['blood', 'product_type']
        widgets = {
            'blood': forms.HiddenInput(),
            'product_type': forms.Select(
                attrs={'class': 'input-xxlarge form-control'})
        }


class BloodForm(forms.ModelForm):

    class Meta:
        model = Blood
        fields = [
            'weight', 'weight_unit', 'height', 'height_unit',
            'haemoglobin', 'haemoglobin_unit', 'blood_pressure',
            'blood_pressure_unit', 'hospital_batch_no', 'nbts_batch_no',
            'anticoagulant', 'date_taken', 'is_taken'
        ]
