# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
