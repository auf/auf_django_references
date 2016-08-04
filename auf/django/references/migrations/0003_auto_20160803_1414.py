# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_auto_20160803_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bureau',
            name='implantation',
            field=models.ForeignKey(db_column=b'implantation', to='references.Implantation', null=True),
        ),
        migrations.AlterField(
            model_name='bureau',
            name='region',
            field=models.ForeignKey(db_column=b'region', to='references.Region', null=True),
        ),
    ]
