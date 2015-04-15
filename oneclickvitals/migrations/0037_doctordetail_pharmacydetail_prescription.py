# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0036_auto_20150411_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('doctor_first_name', models.CharField(max_length=50)),
                ('doctor_last_name', models.CharField(max_length=50)),
                ('name_suffix', models.CharField(max_length=10)),
                ('prescription_network_id', models.CharField(max_length=13)),
                ('dea', models.CharField(max_length=8)),
                ('doctor_phone_number', models.CharField(max_length=10)),
                ('doctor_address', models.CharField(max_length=100)),
                ('doctor_city', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PharmacyDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('pharmacy_name', models.CharField(max_length=50)),
                ('pharmacy_address', models.CharField(max_length=100)),
                ('pharmacy_city', models.CharField(max_length=50)),
                ('pharmacy_phone_number', models.CharField(max_length=10)),
                ('ncpdp_id', models.CharField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_of_issuance', models.DateField(blank=True, null=True)),
                ('day_supply', models.CharField(max_length=5)),
                ('drug_name', models.CharField(max_length=100)),
                ('drug_strength', models.CharField(max_length=5)),
                ('dosage_form', models.CharField(max_length=20)),
                ('frequency', models.CharField(choices=[('daily', 'Daily'), ('every other day', 'Every Other Day'), ('Twice a Day', 'BID/b.i.d.'), ('Three Times a Day', 'TID/t.id'), ('Four Times a Day', 'QID/q.i.d.'), ('Every Bedtime', 'QHS'), ('Every 4 Hours', 'Q4h'), ('Every 4 to 6 Hours', 'Q4-6h'), ('Every Week', 'QWK')], max_length=10)),
                ('quantity', models.CharField(max_length=6)),
                ('npi_number', models.CharField(max_length=10)),
                ('ndc_number', models.CharField(max_length=11)),
                ('refills', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
