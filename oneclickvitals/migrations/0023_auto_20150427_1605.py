# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneclickvitals', '0022_auto_20150426_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='dosage_form',
            field=models.CharField(null=True, choices=[('po (by mouth)', 'PO (by mouth)'), ('pr (per rectum)', 'PR (per rectum)'), ('im (intramuscular)', 'IM (intramuscular)'), ('iv (intravenous)', 'IV (intravenous)'), ('id (intradermal)', 'ID (intradermal)'), ('in (intranasal)', 'IN (intranasal)'), ('tp (topical)', 'TP (topical)')], max_length=20),
            preserve_default=True,
        ),
    ]
