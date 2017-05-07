# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20151129_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='hashmail',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
        ),
    ]
