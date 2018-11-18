import string

from django.test import TestCase
from django.urls import reverse

from .models import Mineral
from mineralcatalog_search.templatetags import utlity_tags

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
        """
        Tests to make sure the database populationscript works.
        """
        Mineral.ingest_data_from_json_file()
        self.assertEqual(Mineral.objects.count(), 871)

    def test_good_mineral_creation(self):
        """Make sure a mineral model DDL is compatible with django code as it exists in the project."""
        test_record = Mineral.objects.create(**test_good_mineral)
        self.assertEqual(test_record.name, "Dogmite")

    def test_bad_mineral_creation(self):
        """Make sure bad minerals are not created that are not compliant with the schema."""
        with self.assertRaises(TypeError):
            Mineral.objects.create(**test_bad_mineral)


class MineralViewsTests(TestCase):
    def setUp(self):
        Mineral.ingest_data_from_json_file()
        self.test_mineral = Mineral.objects.first()

    def test_mineral_list_view(self):
        """Make sure the mineral index view works."""
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.test_mineral, resp.context['minerals'])

    def test_mineral_detail_view(self):
        """Make sure the mineral detail view works."""
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.test_mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.test_mineral, resp.context['mineral'])

    def test_mineral_random(self):
        """Make sure the random mineral is available."""
        response = self.client.get(reverse('minerals:index'))
        self.assertIn('<a class="minerals__anchor" href="/minerals/', response.content.decode('utf-8'))

    def test_search_by_name(self):
        """
        Test search functionality.  Make sure search doesn't return what it isn't supposed to and does return what
        it is supposed to.
        """
        response = self.client.get(reverse('minerals:search'), {'q': 'Abelsonite'})
        positive_search = '<a class="minerals__anchor" href="/minerals/1/">Abelsonite</a>'
        negative_search = '<a class="minerals__anchor" href="/minerals/7/">Adamite</a>'
        self.assertIn(positive_search, response.content.decode('utf-8'))
        self.assertNotIn(negative_search, response.content.decode('utf-8'))

    def test_categories_returned(self):
        """Make sure categories are in the layout.html."""
        response = self.client.get(reverse('minerals:index'))
        html = response.content.decode('utf-8')
        categories = ['Organic Minerals',
                      'Arsenates',
                      'Halides',
                      'Sulfides',
                      'Silicates',
                      'Other',
                      'Oxides',
                      'Sulfosalts',
                      'Phosphates',
                      'Carbonates',
                      'Sulfates',
                      'Native Elements',
                      'Borates'
                      ]
        for each in categories[:]:
            if each in html:
                categories.remove(each)
        self.assertEqual(len(categories), 0)


class CustomTagTests(TestCase):

    def setUp(self):
        Mineral.ingest_data_from_json_file()

    def test_alphabetical_tag(self):
        """
        Custom tag logic for alphabetical is returning the first few letters of the alphabet for minerals we know to exist.
        For example, we know we have minerals that begin with the letters A, B and C.
        """
        abc = string.ascii_uppercase[:3]
        self.assertIn(abc[0], utlity_tags.alpha_dict().keys())
        self.assertIn(abc[1], utlity_tags.alpha_dict().keys())
        self.assertIn(abc[2], utlity_tags.alpha_dict().keys())
