# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='views',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
