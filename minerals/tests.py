import re

from django.test import TestCase
from django.urls import reverse

from .models import Mineral

test_good_mineral = {"name": "Dogmite",
                     "image_filename": "240px-Copper-21991.jpg",
                     "image_caption": "A dog",
                     "category": "Native metal",
                     "formula": "WOOF",
                     "strunz_classification": "01.AA.05",
                     "crystal_system": "cubic Hexoctahedral",
                     "unit_cell": "a = 3.615 Å = 4",
                     "color": "Many",
                     "crystal_symmetry": "Isometric 4/m 3 2/m",
                     "cleavage": "No",
                     "mohs_scale_hardness": "2",
                     "luster": "No",
                     "streak": "Many different",
                     "diaphaneity": "Opaque",
                     "crystal_habit": "Crystal Meth",
                     "specific_gravity": ".95",
                     "group": "Native Elements"}

test_bad_mineral = {"no_primary_key": "Missinginaction"}

class MineralModelTests(TestCase):

    def test_populate_database(self):
        Mineral.ingest_data_from_json_file()
        self.assertEqual(Mineral.objects.count(), 871)

    def test_good_mineral_creation(self):
        test_record = Mineral.objects.create(**test_good_mineral)
        self.assertEqual(test_record.name, "Dogmite")

    def test_bad_mineral_creation(self):
        with self.assertRaises(TypeError):
            Mineral.objects.create(**test_bad_mineral)


class MineralViewsTests(TestCase):
    def setUp(self):
        Mineral.ingest_data_from_json_file()
        self.test_mineral = Mineral.objects.first()

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.test_mineral, resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.test_mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.test_mineral, resp.context['mineral'])

    def test_mineral_random(self):
        response = self.client.get(reverse('minerals:index'))
        self.assertIn('<a class="minerals__anchor" href="/minerals/', response.content.decode('utf-8'))

#Need to add the additional views to the test cases.
        #Search by name
        #Test more HTML returned.
#Need to add the tags to the test cases.
    #random mineral, mineral dict, alpha dict