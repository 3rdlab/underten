# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150407_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_id',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
