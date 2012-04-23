# encoding: utf-8

from django.test import TestCase

from auf.django.references import models as ref


class ActifsTestCase(TestCase):

    def test_add_region_then_deactivate_then_readd(self):
        self.assertEqual(ref.Region.objects.count(), 0)
        region = ref.Region.objects.create(code='A', nom='Amériques')
        self.assertEqual(ref.Region.objects.count(), 1)
        region.actif = False
        region.save()
        self.assertEqual(ref.Region.objects.count(), 0)
        self.assertEqual(ref.Region.avec_inactifs.count(), 1)
