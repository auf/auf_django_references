# encoding: utf-8

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.models import get_models

class Command(BaseCommand):
    help = 'Synchronise les données de références AUF'

    def handle(self, *args, **options):
        cursor = connection.cursor()
        for model in get_models():
            if model.__module__ == 'auf.django.references.models':
                table_name = model._meta.db_table
                cursor.execute(
                    'CREATE OR REPLACE VIEW `%s` AS SELECT * FROM datamaster.`%s`' % 
                    (table_name, table_name)
                )
