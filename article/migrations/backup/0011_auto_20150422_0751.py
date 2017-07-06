# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20150422_0516'),
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
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
