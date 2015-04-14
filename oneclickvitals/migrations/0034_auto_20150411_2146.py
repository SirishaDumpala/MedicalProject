# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0033_auto_20150410_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tag', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='radiology',
            name='albums',
            field=models.ManyToManyField(blank=True, to='oneclickvitals.Album'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radiology',
            name='tags',
            field=models.ManyToManyField(blank=True, to='oneclickvitals.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='radiology',
            name='caption',
            field=models.CharField(blank=True, max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='radiology',
            name='image',
            field=models.FileField(upload_to='image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='radiology',
            name='title',
            field=models.CharField(blank=True, max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='radiology',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
