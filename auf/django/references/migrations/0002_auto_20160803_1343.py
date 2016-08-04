# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupedirdelegprogrammereg',
            name='region',
            field=models.ForeignKey(db_column=b'region', to='references.Region', null=True),
        ),
    ]
