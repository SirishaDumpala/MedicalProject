# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0018_auto_20150426_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labresults',
            name='bilirubin',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='labresults',
            name='blood',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='labresults',
            name='ketones',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='labresults',
            name='leukocyte_esterase',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='labresults',
            name='nitrite',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='labresults',
            name='urobilinogen',
            field=models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], null=True, max_length=50),
            preserve_default=True,
        ),
    ]
