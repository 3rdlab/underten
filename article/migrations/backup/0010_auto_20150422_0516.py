# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_article_category_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category_id',
        ),
    ]
