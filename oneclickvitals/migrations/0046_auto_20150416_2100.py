# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0045_auto_20150416_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='reason',
            new_name='reason_for_appointment',
        ),
        migrations.AddField(
            model_name='appointment',
            name='type_of_appointment',
            field=models.CharField(null=True, max_length=100, choices=[('routine_preventive_care', 'Routine Preventive Care'), ('follow_up', 'Follow-Up'), ('routine_problem_visit', 'Routine Problem Visit'), ('urgent_same_day_appointment', 'Urgent/Same Day Appointment'), ('nurse_visit', 'Nurse Visit'), ('allergy_shots', 'Allergy Shots'), ('new_patients_and_referrals', 'New Patients and Referrals')]),
            preserve_default=True,
        ),
    ]
