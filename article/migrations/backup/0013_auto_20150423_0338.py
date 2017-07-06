# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20150422_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(to='article.Category'),
            preserve_default=True,
        ),
    ]
