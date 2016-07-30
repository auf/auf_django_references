# encoding: utf-8

import django
from django.db.models.signals import post_syncdb
from django.dispatch import receiver
from auf.django.references import vues_db


# Supprimer les clés étrangères aussi après un migrate
try:
    from south.signals import post_migrate
except ImportError:
    pass
else:
    post_migrate.connect(vues_db.supprimer_cles_etrangeres)

if django.VERSION[0:2] < (1, 7):
    import auf.django.references.models
    from auf.django.references import vues_db
    post_syncdb.connect(vues_db.creer_vues, sender=auf.django.references.models)
    post_syncdb.connect(vues_db.supprimer_cles_etrangeres)