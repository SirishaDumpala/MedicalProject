# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0039_prescription_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctordetail',
            name='user',
        ),
    ]
