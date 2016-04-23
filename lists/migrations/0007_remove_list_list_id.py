# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20160330_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list_id',
        ),
    ]
