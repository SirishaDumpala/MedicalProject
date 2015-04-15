# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0035_radiology_thumbnail2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radiology',
            name='albums',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.RemoveField(
            model_name='radiology',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RemoveField(
            model_name='radiology',
            name='thumbnail2',
        ),
        migrations.AlterField(
            model_name='radiology',
            name='image',
            field=models.ImageField(upload_to='image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='radiology',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
