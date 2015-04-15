# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0040_remove_doctordetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='frequency',
            field=models.CharField(choices=[('daily', 'Daily'), ('every other day', 'Every Other Day'), ('Twice a Day', 'BID/b.i.d.'), ('Three Times a Day', 'TID/t.id'), ('Four Times a Day', 'QID/q.i.d.'), ('Every Bedtime', 'QHS'), ('Every 4 Hours', 'Q4h'), ('Every 4 to 6 Hours', 'Q4-6h'), ('Every Week', 'QWK')], max_length=50),
            preserve_default=True,
        ),
    ]
