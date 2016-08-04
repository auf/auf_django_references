# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_auto_20160803_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetposte',
            name='code_bureau',
        ),
        migrations.RemoveField(
            model_name='projetposte',
            name='code_poste',
        ),
        migrations.RemoveField(
            model_name='projetposte',
            name='code_programme',
        ),
        migrations.RemoveField(
            model_name='projetposte',
            name='code_projet',
        ),
        migrations.DeleteModel(
            name='ProjetPoste',
        ),
    ]
