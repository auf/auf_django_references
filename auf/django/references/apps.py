# -*- encoding: utf-8 -*-

from django.apps import AppConfig
from django.db.models.signals import post_migrate, pre_migrate


class ReferencesConfig(AppConfig):
    name = "auf.django.references"

    # noinspection PyMethodMayBeStatic
    def ready(self):
        from . import vues_db
        pre_migrate.connect(vues_db.creer_vues, sender=self)
        post_migrate.connect(vues_db.supprimer_cles_etrangeres, sender=self)
