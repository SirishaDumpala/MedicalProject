# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0034_auto_20150411_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiology',
            name='thumbnail2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
            preserve_default=True,
        ),
    ]
