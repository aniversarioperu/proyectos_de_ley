# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdl', '0010_auto_20140922_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='titulo_de_ley',
            field=models.TextField(default='', blank=True),
        ),
    ]
