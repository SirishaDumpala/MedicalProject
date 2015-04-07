# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0028_auto_20150402_1958'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='emergencycontact',
            name='relationship',
            field=models.CharField(max_length=50, null=True, choices=[('parent', 'Parent'), ('brother', 'Brother'), ('sister', 'Sister'), ('boyfriend', 'Boyfriend'), ('girlfriend', 'Girlfriend'), ('other', 'Other')]),
            preserve_default=True,
        ),
    ]
