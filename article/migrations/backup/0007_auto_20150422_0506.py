# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_remove_article_short_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('category_name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.SmallIntegerField(default=datetime.datetime(2015, 4, 22, 5, 6, 53, 785759, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
