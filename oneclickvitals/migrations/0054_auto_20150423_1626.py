# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0053_auto_20150423_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='type_of_appointment',
            field=models.CharField(null=True, choices=[('Routine Preventive Care', 'Routine Preventive Care'), ('Follow-Up', 'Follow-Up'), ('Routine Problem Visit', 'Routine Problem Visit'), ('Urgent/Same Day Appointment', 'Urgent/Same Day Appointment'), ('Nurse Visit', 'Nurse Visit'), ('Allergy Shots', 'Allergy Shots'), ('New Patients and Referrals', 'New Patients and Referrals')], max_length=100),
            preserve_default=True,
        ),
    ]
