# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name=b'date published')),
                ('modified_date', models.DateTimeField(null=True)),
                ('ups', models.PositiveSmallIntegerField(default=0)),
                ('downs', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ManyToManyField(to='product.Product', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
