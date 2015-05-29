# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField()),
                ('weight_unit', models.CharField(max_length=3, choices=[(b'kg', b'Kilograms'), (b'lb', b'Pounds')])),
                ('height', models.IntegerField()),
                ('height_unit', models.CharField(max_length=3, choices=[(b'cm', b'Centimeters'), (b'ft', b'Feet')])),
                ('haemoglobin', models.IntegerField()),
                ('haemoglobin_unit', models.CharField(max_length=3, choices=[(b'g/L', b'Gram per Liter')])),
                ('blood_pressure', models.IntegerField()),
                ('blood_pressure_unit', models.CharField(max_length=3, choices=[(b'mmHg', b'Millimeters of Mercury')])),
                ('hospital_batch_no', models.CharField(max_length=50)),
                ('nbts_batch_no', models.CharField(max_length=50)),
                ('anticoagulant', models.CharField(max_length=4, choices=[(b'NaCH', b'Sodium Citrate')])),
                ('date_taken', models.DateField()),
                ('is_taken', models.BooleanField(default=False)),
                ('is_nbts_approved', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BloodProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_type', models.CharField(max_length=4, choices=[(b'RBC', b'Red Blood Cells'), (b'PLATELETS', b'Platelets'), (b'PLASMA', b'Plasma')])),
                ('blood', models.ForeignKey(related_name='products', to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=50)),
                ('age', models.SmallIntegerField()),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('blood_group', models.CharField(max_length=2, choices=[(b'A', b'A'), (b'B', b'B'), (b'O', b'O'), (b'AB', b'AB')])),
                ('is_rh_positive', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DonorConditionFormA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('advised_against_giving', models.BooleanField(default=False)),
                ('anaemia', models.BooleanField(default=False)),
                ('serious_illness', models.BooleanField(default=False)),
                ('neurosurgical_procedure', models.BooleanField(default=False)),
                ('transplant', models.BooleanField(default=False)),
                ('growth_hormone', models.BooleanField(default=False)),
                ('head_injury', models.BooleanField(default=False)),
                ('blood_pressure_issue', models.BooleanField(default=False)),
                ('bowel_disease', models.BooleanField(default=False)),
                ('kidney_problem', models.BooleanField(default=False)),
                ('diabetes', models.BooleanField(default=False)),
                ('cancer', models.BooleanField(default=False)),
                ('malaria', models.BooleanField(default=False)),
                ('jaundice', models.BooleanField(default=False)),
                ('tigason', models.BooleanField(default=False)),
                ('blood', models.OneToOneField(to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DonorConditionFormB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feeling_healthy', models.BooleanField(default=False)),
                ('ever_pregnant', models.BooleanField(default=False)),
                ('pregnancy_count', models.SmallIntegerField(default=0)),
                ('recent_pregnancy', models.BooleanField(default=False)),
                ('risk_of_injury_activities', models.BooleanField(default=False)),
                ('dental_work', models.BooleanField(default=False)),
                ('pain_killers', models.BooleanField(default=False)),
                ('cuts', models.BooleanField(default=False)),
                ('gastric_upset', models.BooleanField(default=False)),
                ('recent_unwellness', models.BooleanField(default=False)),
                ('recent_chest_pain', models.BooleanField(default=False)),
                ('recent_skin_condition', models.BooleanField(default=False)),
                ('recent_medication', models.BooleanField(default=False)),
                ('recent_abattoir', models.BooleanField(default=False)),
                ('recent_sexual_infection', models.BooleanField(default=False)),
                ('recent_immunizations', models.BooleanField(default=False)),
                ('recent_chicken_pox', models.BooleanField(default=False)),
                ('blood', models.OneToOneField(to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DonorConditionFormC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aids', models.BooleanField(default=False)),
                ('unprescibed_injection', models.BooleanField(default=False)),
                ('clotting_factors', models.BooleanField(default=False)),
                ('hepatitis', models.BooleanField(default=False)),
                ('swollen_glands', models.BooleanField(default=False)),
                ('sex_with_above', models.BooleanField(default=False)),
                ('blood_transfusion', models.BooleanField(default=False)),
                ('injured_with_needle', models.BooleanField(default=False)),
                ('tatoo', models.BooleanField(default=False)),
                ('blood', models.OneToOneField(to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DonorConditionPreForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_first_donation', models.BooleanField(default=True)),
                ('last_donation_place', models.CharField(max_length=150)),
                ('last_donation_date', models.DateField()),
                ('blood', models.OneToOneField(to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HospitalTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blood_type_crossmatch', models.BooleanField(default=False)),
                ('adverse_antibodies', models.BooleanField(default=False)),
                ('infectious_agents', models.BooleanField(default=False)),
                ('blood_group_antibodies', models.BooleanField(default=False)),
                ('hiv1', models.BooleanField(default=False)),
                ('hiv2', models.BooleanField(default=False)),
                ('htlv_I', models.BooleanField(default=False)),
                ('htlv_II', models.BooleanField(default=False)),
                ('hepatitis_B', models.BooleanField(default=False)),
                ('hepatitis_C', models.BooleanField(default=False)),
                ('syphillis', models.BooleanField(default=False)),
                ('west_nile', models.BooleanField(default=False)),
                ('chagas', models.BooleanField(default=False)),
                ('blood', models.OneToOneField(to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NBTSTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blood_type_crossmatch', models.BooleanField(default=False)),
                ('adverse_antibodies', models.BooleanField(default=False)),
                ('infectious_agents', models.BooleanField(default=False)),
                ('blood_group_antibodies', models.BooleanField(default=False)),
                ('hiv1', models.BooleanField(default=False)),
                ('hiv2', models.BooleanField(default=False)),
                ('htlv_I', models.BooleanField(default=False)),
                ('htlv_II', models.BooleanField(default=False)),
                ('hepatitis_B', models.BooleanField(default=False)),
                ('hepatitis_C', models.BooleanField(default=False)),
                ('syphillis', models.BooleanField(default=False)),
                ('west_nile', models.BooleanField(default=False)),
                ('chagas', models.BooleanField(default=False)),
                ('blood', models.OneToOneField(to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blood',
            name='donor',
            field=models.ForeignKey(related_name='donated_blood', to='donations.Donor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blood',
            name='hospital',
            field=models.ForeignKey(related_name='bloods', to='users.Hospital'),
            preserve_default=True,
        ),
    ]
