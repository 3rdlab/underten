# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_remove_article_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
