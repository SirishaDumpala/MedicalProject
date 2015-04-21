# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_localflavor_us.models


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0058_auto_20150419_1657'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PharmacyDetail',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='day_supply',
            new_name='days_supply',
        ),
        migrations.RemoveField(
            model_name='doctordetail',
            name='doctor_address',
        ),
        migrations.RemoveField(
            model_name='doctordetail',
            name='doctor_city',
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='address_1',
            field=models.CharField(verbose_name='address', max_length=128, default='Grand Pasteur Clinic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='address_2',
            field=models.CharField(verbose_name="address cont'd", max_length=128, default='515 Hamilton Ave'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='city',
            field=models.CharField(verbose_name='city', max_length=64, default='Fullerton'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='state',
            field=django_localflavor_us.models.USStateField(verbose_name='state', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2, default='CA'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctordetail',
            name='zip_code',
            field=models.CharField(verbose_name='zip code', max_length=5, default='92652'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_phone_number',
            field=models.CharField(max_length=14, default='(717) 444-0880'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='contact_phone_number',
            field=models.CharField(max_length=14, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='pharmacy_phone_number',
            field=models.CharField(max_length=14, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='date_of_issuance',
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
