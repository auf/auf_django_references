# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0005_auto_20160803_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentification',
            name='id',
            field=models.OneToOneField(primary_key=True, db_column=b'id', serialize=False, to='references.Employe'),
        ),
    ]
