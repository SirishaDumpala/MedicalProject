# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0036_userdetail_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('complaint', models.TextField(max_length=500)),
                ('additional_comments', models.TextField(max_length=500)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='patientmedicalhistory',
            name='social_habits',
            field=models.CharField(max_length=50, choices=[('smoking', 'Smoking'), ('alcohol', 'Alcohol'), ('exercise', 'Exercise'), ('street drugs', 'Street Drugs'), ('other', 'Other'), ('none', 'None')]),
            preserve_default=True,
        ),
    ]
