# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0021_labtest_test_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labresults',
            name='test_type',
            field=models.CharField(max_length=50, null=True, choices=[('urine culture', 'Urine Culture'), ('blood culture', 'Blood Culture'), ('allergy test', 'Allergy Test'), ('blood glucose', 'Blood Glucose'), ('thyroid', 'Thyroid'), ('pregnancy test', 'Pregnancy Test')]),
            preserve_default=True,
        ),
    ]
