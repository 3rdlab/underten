# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20150422_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category_id',
        ),
    ]
