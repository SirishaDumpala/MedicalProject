# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oneclickvitals', '0063_diagnosis_diagnosis'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('urine_culture', models.NullBooleanField()),
                ('blood_culture', models.NullBooleanField()),
                ('allergy_test', models.NullBooleanField()),
                ('blood_glucose', models.NullBooleanField()),
                ('thyroid', models.NullBooleanField()),
                ('viral_test', models.NullBooleanField()),
                ('pregnancy_test', models.NullBooleanField()),
                ('x_ray', models.CharField(choices=[('finger', 'Finger'), ('palm', 'Palm'), ('wrist', 'Wrist'), ('right elbow', 'Right Elbow'), ('left elbow', 'Left Elbow'), ('right shoulder', 'Right Shoulder'), ('neck', 'Neck'), ('upper back', 'Upper Back'), ('middle back', 'Middle Back'), ('lower back', 'Lower Back'), ('right knee', 'Right Knee'), ('left knee', 'Left Knee'), ('right leg', 'Right leg'), ('left leg', 'Left Leg'), ('right ankle', 'Right Ankle'), ('left ankle', 'Left Ankle'), ('right foot', 'Right Foot'), ('left foot', 'Left Foot'), ('other', 'Other'), ('none', 'None')], max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='lab_test',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
