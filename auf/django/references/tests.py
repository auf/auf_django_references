# encoding: utf-8

from __future__ import absolute_import

from django.core import management
from django.db import models
from django.test import TestCase

from auf.django.references import models as ref
from tests.universite.models import Universite


class EtablissementBaseTestCase(TestCase):
    fixtures = ['tests.yaml']

    def test_add_universite(self):
        canada = ref.Pays.objects.get(code='CA')
        uqam = Universite.objects.create(nom='UQAM', pays=canada, recteur='Claude Corbo')
        self.assertEqual(uqam.ref, None)
        self.assertEqual(Universite.objects.count(), 1)

    def test_create_universite_from_etablissement(self):
        etablissement = ref.Etablissement.objects.get(nom='Université de Montréal')
        udem = Universite.objects.create(ref=etablissement, recteur='Guy Breton')
        self.assertEqual(udem.nom, u'Université de Montréal')
        self.assertEqual(udem.pays.nom, u'Canada')
        self.assertEqual(udem.recteur, u'Guy Breton')
        self.assertEqual(udem.ref, etablissement)

    def test_sync_references(self):
        etablissement = ref.Etablissement.objects.get(nom='Université de Montréal')
        udem = Universite.objects.create(ref=etablissement, recteur='Guy Breton')
        self.assertEqual(udem.nom, u'Université de Montréal')
        self.assertEqual(udem.pays.nom, u'Canada')
        udem.save()
        etablissement.nom = 'UdeM'
        etablissement.pays = ref.Pays.objects.get(code='FR')
        etablissement.save()
        management.call_command('sync_references')
        udem2 = Universite.objects.get(pk=udem.pk)
        self.assertEqual(udem2.nom, u'UdeM')
        self.assertEqual(udem2.pays.nom, u'France')
        self.assertEqual(udem2.recteur, u'Guy Breton')
