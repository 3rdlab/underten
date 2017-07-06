# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150526_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='docfile',
            field=models.FileField(null=True, upload_to=b'media/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
