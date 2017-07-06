# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_article_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_text',
            field=redactor.fields.RedactorField(default=datetime.datetime(2015, 4, 20, 4, 28, 4, 879359, tzinfo=utc), verbose_name='Text'),
            preserve_default=False,
        ),
    ]
