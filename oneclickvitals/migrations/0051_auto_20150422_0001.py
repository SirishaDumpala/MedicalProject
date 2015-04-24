# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0050_auto_20150421_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('urine_culture', models.NullBooleanField()),
                ('blood_culture', models.NullBooleanField()),
                ('allergy_test', models.NullBooleanField()),
                ('blood_glucose', models.NullBooleanField()),
                ('thyroid', models.NullBooleanField()),
                ('viral_test', models.NullBooleanField()),
                ('pregnancy_test', models.NullBooleanField()),
                ('x_ray', models.CharField(choices=[('finger', 'Finger'), ('palm', 'Palm'), ('wrist', 'Wrist'), ('right elbow', 'Right Elbow'), ('left elbow', 'Left Elbow'), ('right shoulder', 'Right Shoulder'), ('neck', 'Neck'), ('upper back', 'Upper Back'), ('middle back', 'Middle Back'), ('lower back', 'Lower Back'), ('right knee', 'Right Knee'), ('left knee', 'Left Knee'), ('right leg', 'Right leg'), ('left leg', 'Left Leg'), ('right ankle', 'Right Ankle'), ('left ankle', 'Left Ankle'), ('right foot', 'Right Foot'), ('left foot', 'Left Foot'), ('other', 'Other'), ('none', 'None')], max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='reason',
            new_name='reason_for_appointment',
        ),
        migrations.RemoveField(
            model_name='doctordetail',
            name='doctor_address',
        ),
        migrations.RemoveField(
            model_name='doctordetail',
            name='doctor_city',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='contact_address',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='contact_city',
        ),
        migrations.RemoveField(
            model_name='pharmacydetail',
            name='ncpdp_id',
        ),
        migrations.RemoveField(
            model_name='pharmacydetail',
            name='pharmacy_address',
        ),
        migrations.RemoveField(
            model_name='pharmacydetail',
            name='pharmacy_city',
        ),
        migrations.RemoveField(
            model_name='pharmacydetail',
            name='pharmacy_email',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='address',
        ),
        migrations.AddField(
            model_name='appointment',
            name='type_of_appointment',
            field=models.CharField(choices=[('routine_preventive_care', 'Routine Preventive Care'), ('follow_up', 'Follow-Up'), ('routine_problem_visit', 'Routine Problem Visit'), ('urgent_same_day_appointment', 'Urgent/Same Day Appointment'), ('nurse_visit', 'Nurse Visit'), ('allergy_shots', 'Allergy Shots'), ('new_patients_and_referrals', 'New Patients and Referrals')], max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='address_1',
            field=models.CharField(default='Grand Pasteur Clinic', max_length=128, verbose_name='address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='address_2',
            field=models.CharField(default='515 Hamilton Ave', max_length=128, verbose_name="address cont'd"),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='city',
            field=models.CharField(default='Fullerton', max_length=64, verbose_name='city'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='state',
            field=localflavor.us.models.USStateField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='CA', max_length=2, verbose_name='state'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='zip_code',
            field=models.CharField(default='92652', max_length=5, verbose_name='zip code'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='address_1',
            field=models.CharField(max_length=128, verbose_name='address', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='address_2',
            field=models.CharField(max_length=128, verbose_name="address cont'd", blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='city',
            field=models.CharField(default='Fullerton', max_length=64, verbose_name='city'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='state',
            field=localflavor.us.models.USStateField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='CA', max_length=2, verbose_name='state'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='zip_code',
            field=models.CharField(default='92614', max_length=5, verbose_name='zip code'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patientmedicalhistory',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=4, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patientmedicalhistory',
            name='chief_complaint',
            field=models.TextField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patientmedicalhistory',
            name='height',
            field=models.PositiveIntegerField(max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patientmedicalhistory',
            name='weight',
            field=models.FloatField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pharmacydetail',
            name='address_1',
            field=models.CharField(max_length=128, verbose_name='address', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pharmacydetail',
            name='address_2',
            field=models.CharField(max_length=128, verbose_name="address cont'd", blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pharmacydetail',
            name='city',
            field=models.CharField(default='Fullerton', max_length=64, verbose_name='city'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pharmacydetail',
            name='state',
            field=localflavor.us.models.USStateField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='CA', max_length=2, verbose_name='state'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pharmacydetail',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pharmacydetail',
            name='zip_code',
            field=models.CharField(default='92614', max_length=5, verbose_name='zip code'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='address_1',
            field=models.CharField(max_length=128, verbose_name='address', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='address_2',
            field=models.CharField(max_length=128, verbose_name="address cont'd", blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='state',
            field=localflavor.us.models.USStateField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], default='CA', max_length=2, verbose_name='state'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='zip_code',
            field=models.CharField(default='92614', max_length=5, verbose_name='zip code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_phone_number',
            field=models.CharField(default='(717) 444-0880', max_length=14),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pharmacydetail',
            name='pharmacy_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pharmacydetail',
            name='pharmacy_phone_number',
            field=models.CharField(max_length=14, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='city',
            field=models.CharField(default='Fullerton', max_length=64, verbose_name='city'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='phone_number',
            field=models.CharField(max_length=14, null=True),
            preserve_default=True,
        ),
    ]
