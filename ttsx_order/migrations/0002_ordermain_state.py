# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='state',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
