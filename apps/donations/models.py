from django.db import models

from apps.users.models import Hospital
from bloodbank.utils import options


class Donor(models.Model):

    name = models.CharField(max_length=150)
    number = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    gender = models.CharField(
        max_length=1, choices=options.GENDER)
    blood_group = models.CharField(
        max_length=2, choices=options.BLOOD_GROUPS, blank=True, null=True)
    is_rh_positive = models.BooleanField(
        default=False, choices=options.YES_NO)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Blood(models.Model):

    donor = models.ForeignKey(Donor, related_name='donated_blood')

    weight = models.IntegerField(blank=True, null=True)
    weight_unit = models.CharField(
        max_length=3, choices=options.WEIGHT_UNITS, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    height_unit = models.CharField(
        max_length=3, choices=options.HEIGHT_UNITS, blank=True, null=True)
    haemoglobin = models.IntegerField(blank=True, null=True)
    haemoglobin_unit = models.CharField(
        max_length=3, choices=options.HAEMOGLOBIN_UNITS, blank=True, null=True)
    blood_pressure = models.IntegerField(blank=True, null=True)
    blood_pressure_unit = models.CharField(
        max_length=3, choices=options.BLOOD_PRESSURE_UNITS,
        blank=True, null=True)

    hospital_batch_no = models.CharField(max_length=50, blank=True, null=True)
    nbts_batch_no = models.CharField(max_length=50, blank=True, null=True)
    anticoagulant = models.CharField(
        max_length=4, choices=options.ANTICOAGULANTS, blank=True, null=True)
    date_taken = models.DateField()
    is_taken = models.BooleanField(
        default=False, choices=options.YES_NO)
    is_nbts_approved = models.BooleanField(
        default=False, choices=options.YES_NO)
    hospital = models.ForeignKey(Hospital, related_name='bloods')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class DonorConditionPreForm(models.Model):

    blood = models.OneToOneField(Blood)
    is_first_donation = models.BooleanField(
        default=True, choices=options.YES_NO)
    last_donation_place = models.CharField(
        max_length=150, blank=True, null=True)
    last_donation_date = models.DateField(blank=True, null=True)


class DonorConditionFormA(models.Model):

    blood = models.OneToOneField(Blood)
    advised_against_giving = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever been advised not to give blood?')
    anaemia = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever suffered from anaemia or any blood disorder?')
    serious_illness = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever had a serious illness,operation or been admitted to hospital?')
    neurosurgical_procedure = models.BooleanField(
        default=False, choices=options.YES_NO,
)
    transplant = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever recieved a transplant or graft(organ,bone marrow,cornea etc?')
    growth_hormone = models.BooleanField(
        default=False, choices=options.YES_NO)
    head_injury = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever suffered from a head injury, stroke or epilepsy?')
    blood_pressure_issue = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever had a heart or blood pressure problem, chest pain, rheumatic fever or a heart murmur?')
    bowel_disease = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever had a bowel disease,stomach or duodenal problems or ulcers?')
    kidney_problem = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever had kedney, liver or lung problems including tuberclosis (TB)?')
    diabetes = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever had diabetes, a thyroid disorder?')
    cancer = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='ever had cancer of any kind?')
    malaria = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever had malaria recently?')
    jaundice = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Ever had jaundice (yellow eyes/skin) or hepatitis?')
    tigason = models.BooleanField(
        default=False, choices=options.YES_NO)


class DonorConditionFormB(models.Model):

    blood = models.OneToOneField(Blood)
    feeling_healthy = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Are you feeling healthy and well?')
    ever_pregnant = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Have you ever been pregnant (including miscarriage and termination of pregnancy)?')
    pregnancy_count = models.SmallIntegerField(default=0)
    recent_pregnancy = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Have you been pregnant in the last 9 months?')
    risk_of_injury_activities = models.BooleanField(
        default=False, choices=options.YES_NO)
    dental_work = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Had dental work, cleaning, fillings or extractions?')
    pain_killers = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Taken any aspirin, pain killers or anti-inflammatory preparations?')
    cuts = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Had any cuts, abrasions, sores or rashes?')
    gastric_upset = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Had any gastric upset, diarrhoea, abdominal pain or vomiting?')
    recent_unwellness = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Been well, or seen a doctor or any other health care practioner, had an operation(surgical procedure) or any tests/investigation?')
    recent_chest_pain = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Had any chest pain/angina or an irregular heartbeat?')
    recent_skin_condition = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Taken tablets for acne or a skin condition?')
    recent_medication = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Taken any medication, including regular or clinical trial medication?')
    recent_abattoir = models.BooleanField(
        default=False, choices=options.YES_NO)
    recent_sexual_infection = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Had a sexually transmitted infection e.g. gonorrhoea, syphilis or genital herpes?')
    recent_immunizations = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Had any immunisations/vaccinations including as part of a clinical trial?')
    recent_chicken_pox = models.BooleanField(
        default=False, choices=options.YES_NO,
        verbose_name='Had chickenpox?')


class DonorConditionFormC(models.Model):

    blood = models.OneToOneField(Blood)
    aids = models.BooleanField(
        default=False, choices=options.YES_NO)
    unprescibed_injection = models.BooleanField(
        default=False, choices=options.YES_NO ,verbose_name="Have you had any unprescibed_injection?")
    clotting_factors = models.BooleanField(
        default=False, choices=options.YES_NO)
    hepatitis = models.BooleanField(
        default=False, choices=options.YES_NO)
    swollen_glands = models.BooleanField(
        default=False, choices=options.YES_NO)
    sex_with_above = models.BooleanField(
        default=False, choices=options.YES_NO)
    blood_transfusion = models.BooleanField(
        default=False, choices=options.YES_NO)
    injured_with_needle = models.BooleanField(
        default=False, choices=options.YES_NO)
    tatoo = models.BooleanField(
        default=False, choices=options.YES_NO)


class BloodProduct(models.Model):

    blood = models.ForeignKey(Blood, related_name='products')
    product_type = models.CharField(
        max_length=4, choices=options.BLOOD_PRODUCT_TYPES)


class HospitalTest(models.Model):

    blood = models.OneToOneField(Blood)
    blood_type_crossmatch = models.BooleanField(
        default=False, choices=options.YES_NO)
    adverse_antibodies = models.BooleanField(
        default=False, choices=options.YES_NO)
    infectious_agents = models.BooleanField(
        default=False, choices=options.YES_NO)
    blood_group_antibodies = models.BooleanField(
        default=False, choices=options.YES_NO)
    hiv1 = models.BooleanField(
        default=False, choices=options.YES_NO)
    hiv2 = models.BooleanField(
        default=False, choices=options.YES_NO)
    htlv_I = models.BooleanField(
        default=False, choices=options.YES_NO)
    htlv_II = models.BooleanField(
        default=False, choices=options.YES_NO)
    hepatitis_B = models.BooleanField(
        default=False, choices=options.YES_NO)
    hepatitis_C = models.BooleanField(
        default=False, choices=options.YES_NO)
    syphillis = models.BooleanField(
        default=False, choices=options.YES_NO)
    west_nile = models.BooleanField(
        default=False, choices=options.YES_NO)
    chagas = models.BooleanField(
        default=False, choices=options.YES_NO)


class NBTSTest(models.Model):

    blood = models.OneToOneField(Blood)
    blood_type_crossmatch = models.BooleanField(
        default=False, choices=options.YES_NO)
    adverse_antibodies = models.BooleanField(
        default=False, choices=options.YES_NO)
    infectious_agents = models.BooleanField(
        default=False, choices=options.YES_NO)
    blood_group_antibodies = models.BooleanField(
        default=False, choices=options.YES_NO)
    hiv1 = models.BooleanField(
        default=False, choices=options.YES_NO)
    hiv2 = models.BooleanField(
        default=False, choices=options.YES_NO)
    htlv_I = models.BooleanField(
        default=False, choices=options.YES_NO)
    htlv_II = models.BooleanField(
        default=False, choices=options.YES_NO)
    hepatitis_B = models.BooleanField(
        default=False, choices=options.YES_NO)
    hepatitis_C = models.BooleanField(
        default=False, choices=options.YES_NO)
    syphillis = models.BooleanField(
        default=False, choices=options.YES_NO)
    west_nile = models.BooleanField(
        default=False, choices=options.YES_NO)
    chagas = models.BooleanField(
        default=False, choices=options.YES_NO)
