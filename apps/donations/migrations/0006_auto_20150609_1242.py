# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_auto_20150529_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='NBGSTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blood_type_crossmatch', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('adverse_antibodies', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('infectious_agents', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('blood_group_antibodies', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('hiv1', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('hiv2', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('htlv_I', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('htlv_II', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('hepatitis_B', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('hepatitis_C', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('syphillis', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('west_nile', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('chagas', models.BooleanField(default=False, choices=[(True, b'Yes'), (False, b'No')])),
                ('blood', models.OneToOneField(to='donations.Blood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='nbtstest',
            name='blood',
        ),
        migrations.DeleteModel(
            name='NBTSTest',
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='anaemia',
            field=models.BooleanField(default=False, verbose_name=b'Ever suffered from anaemia or any blood disorder?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='blood_pressure_issue',
            field=models.BooleanField(default=False, verbose_name=b'Ever had a heart or blood pressure problem, chest pain, rheumatic fever or a heart murmur?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='bowel_disease',
            field=models.BooleanField(default=False, verbose_name=b'Ever had a bowel disease,stomach or duodenal problems or ulcers?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='cancer',
            field=models.BooleanField(default=False, verbose_name=b'ever had cancer of any kind?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='diabetes',
            field=models.BooleanField(default=False, verbose_name=b'Ever had diabetes, a thyroid disorder?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='head_injury',
            field=models.BooleanField(default=False, verbose_name=b'Ever suffered from a head injury, stroke or epilepsy?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='jaundice',
            field=models.BooleanField(default=False, verbose_name=b'Ever had jaundice (yellow eyes/skin) or hepatitis?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='kidney_problem',
            field=models.BooleanField(default=False, verbose_name=b'Ever had kedney, liver or lung problems including tuberclosis (TB)?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='malaria',
            field=models.BooleanField(default=False, verbose_name=b'Ever had malaria recently?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='serious_illness',
            field=models.BooleanField(default=False, verbose_name=b'Ever had a serious illness,operation or been admitted to hospital?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionforma',
            name='transplant',
            field=models.BooleanField(default=False, verbose_name=b'Ever recieved a transplant or graft(organ,bone marrow,cornea etc?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='cuts',
            field=models.BooleanField(default=False, verbose_name=b'Had any cuts, abrasions, sores or rashes?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='dental_work',
            field=models.BooleanField(default=False, verbose_name=b'Had dental work, cleaning, fillings or extractions?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='ever_pregnant',
            field=models.BooleanField(default=False, verbose_name=b'Have you ever been pregnant (including miscarriage and termination of pregnancy)?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='feeling_healthy',
            field=models.BooleanField(default=False, verbose_name=b'Are you feeling healthy and well?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='gastric_upset',
            field=models.BooleanField(default=False, verbose_name=b'Had any gastric upset, diarrhoea, abdominal pain or vomiting?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='pain_killers',
            field=models.BooleanField(default=False, verbose_name=b'Taken any aspirin, pain killers or anti-inflammatory preparations?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_chest_pain',
            field=models.BooleanField(default=False, verbose_name=b'Had any chest pain/angina or an irregular heartbeat?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_chicken_pox',
            field=models.BooleanField(default=False, verbose_name=b'Had chickenpox?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_immunizations',
            field=models.BooleanField(default=False, verbose_name=b'Had any immunisations/vaccinations including as part of a clinical trial?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_medication',
            field=models.BooleanField(default=False, verbose_name=b'Taken any medication, including regular or clinical trial medication?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_pregnancy',
            field=models.BooleanField(default=False, verbose_name=b'Have you been pregnant in the last 9 months?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_sexual_infection',
            field=models.BooleanField(default=False, verbose_name=b'Had a sexually transmitted infection e.g. gonorrhoea, syphilis or genital herpes?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_skin_condition',
            field=models.BooleanField(default=False, verbose_name=b'Taken tablets for acne or a skin condition?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformb',
            name='recent_unwellness',
            field=models.BooleanField(default=False, verbose_name=b'Been well, or seen a doctor or any other health care practioner, had an operation(surgical procedure) or any tests/investigation?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='donorconditionformc',
            name='unprescibed_injection',
            field=models.BooleanField(default=False, verbose_name=b'Have you had any unprescibed_injection?', choices=[(True, b'Yes'), (False, b'No')]),
            preserve_default=True,
        ),
    ]
