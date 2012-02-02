# encoding: utf-8

from django.db import connection
from django.db.models import get_models, signals
from django.conf import settings

import auf.django.references.models

def post_syncdb(sender, **kwargs):
    if 'auf.django.references.managedref' not in settings.INSTALLED_APPS:
        print u'Création des vues pour les données de référence...'
        cursor = connection.cursor()
        for model in get_models():
            if model.__module__ == 'auf.django.references.models':
                table_name = model._meta.db_table
                cursor.execute(
                    'CREATE OR REPLACE VIEW `%s` AS SELECT * FROM datamaster.`%s`' %
                    (table_name, table_name)
                )

signals.post_syncdb.connect(post_syncdb, sender=auf.django.references.models)
