# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0042_pharmacydetail_pharmacy_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('complaint', models.TextField(max_length=500)),
                ('diagnosis', models.TextField(max_length=1000)),
                ('additional_comments', models.TextField(max_length=500)),
                ('follow_up', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FamilyMedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('stroke', models.NullBooleanField()),
                ('cancer', models.NullBooleanField()),
                ('high_bp', models.NullBooleanField()),
                ('tuberculosis', models.NullBooleanField()),
                ('diabetes', models.NullBooleanField()),
                ('leukemia', models.NullBooleanField()),
                ('bleeding_tendency', models.NullBooleanField()),
                ('heart_attack', models.NullBooleanField()),
                ('kidney_disease', models.NullBooleanField()),
                ('rheumatic_heart', models.NullBooleanField()),
                ('heart_failure', models.NullBooleanField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VitalSigns',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('visit_date', models.DateField(default=django.utils.timezone.now)),
                ('heart_rate', models.TextField(max_length=5)),
                ('blood_pressure', models.TextField(max_length=5)),
                ('temperature', models.TextField(max_length=5)),
                ('current_weight', models.TextField(max_length=5)),
                ('current_height', models.TextField(max_length=5)),
                ('notes', models.TextField(max_length=500)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient_vital_signs',
            field=models.OneToOneField(to='oneclickvitals.VitalSigns'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='emergencycontact',
            old_name='phone_number',
            new_name='contact_phone_number',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='city',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patientmedicalhistory',
            name='chief_complaint',
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='contact_address',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='contact_city',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='contact_first_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='contact_last_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='gender',
            field=models.CharField(max_length=50, null=True, choices=[('female', 'Female'), ('male', 'Male')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.CharField(max_length=50, null=True, choices=[('spouse', 'Spouse'), ('parent', 'Parent'), ('brother', 'Brother'), ('sister', 'Sister'), ('boyfriend', 'Boyfriend'), ('girlfriend', 'Girlfriend'), ('other', 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='social_habits',
            field=models.CharField(max_length=50, choices=[('smoking', 'Smoking'), ('alcohol', 'Alcohol'), ('exercise', 'Exercise'), ('street drugs', 'Street drugs'), ('other', 'Other'), ('none', 'None')]),
            preserve_default=True,
        ),
    ]
