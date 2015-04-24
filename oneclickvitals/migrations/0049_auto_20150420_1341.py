# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0048_auto_20150417_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
