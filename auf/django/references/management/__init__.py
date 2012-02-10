# encoding: utf-8

from django import db
from django.db.models import get_models, signals
from django.conf import settings

import auf.django.references.models

def post_syncdb(sender, **kwargs):
    """Création des vues vers datamaster."""

    # On ne crée des vues que si on est sur une BD MySQL.
    # L'attribut db.connection.vendor n'est présent qu'à partir de Django
    # 1.3
    if (hasattr(db.connection, 'vendor') and db.connection.vendor != 'mysql') or \
       'mysql' not in db.backend.__name__:
        return

    cursor = db.connection.cursor()

    # Vérifions qu'on a une BD qui s'appelle 'datamaster'
    if not cursor.execute("SHOW DATABASES LIKE 'datamaster'"):
        return

    # Déterminons la liste de tables de référence dans datamaster
    cursor.execute("SHOW TABLES IN datamaster LIKE 'ref\\_%%'")
    datamaster_tables = set(row[0] for row in cursor)

    # Déterminons la liste de tables que nous avons déjà et
    # enlevons-les des tables de datamaster
    cursor.execute("SHOW FULL TABLES WHERE Table_type != 'VIEW'")
    my_tables = set(row[0] for row in cursor)
    datamaster_tables.difference_update(my_tables)

    # On peut maintenant créer les vues
    cursor = db.connection.cursor()
    for table in datamaster_tables:
        print u"Création d'une vue vers datamaster.%s" % table
        cursor.execute(
            'CREATE OR REPLACE VIEW `%s` AS SELECT * FROM datamaster.`%s`' % (table, table)
        )

signals.post_syncdb.connect(post_syncdb, sender=auf.django.references.models)
