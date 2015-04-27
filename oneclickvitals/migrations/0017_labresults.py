# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0016_auto_20150424_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabResults',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('test_type', models.CharField(max_length=50, choices=[('urine culture', 'Urine Culture'), ('blood culture', 'Blood Culture'), ('allergy test', 'Allergy Test'), ('blood glucose', 'Blood Glucose'), ('thyroid', 'Thyroid'), ('pregnancy test', 'Pregnancy Test')])),
                ('specific_gravity', models.FloatField(null=True, max_length=6)),
                ('pH', models.FloatField(null=True, max_length=4)),
                ('protein', models.PositiveIntegerField(null=True, max_length=3)),
                ('glucose', models.PositiveIntegerField(null=True, max_length=3)),
                ('ketones', models.CharField(max_length=50, choices=[('positive', 'Positive'), ('negative', 'Negative')])),
                ('blood', models.CharField(max_length=50, choices=[('positive', 'Positive'), ('negative', 'Negative')])),
                ('leukocyte_esterase', models.CharField(max_length=50, choices=[('positive', 'Positive'), ('negative', 'Negative')])),
                ('nitrite', models.CharField(max_length=50, choices=[('positive', 'Positive'), ('negative', 'Negative')])),
                ('bilirubin', models.CharField(max_length=50, choices=[('positive', 'Positive'), ('negative', 'Negative')])),
                ('urobilinogen', models.CharField(max_length=50, choices=[('positive', 'Positive'), ('negative', 'Negative')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
