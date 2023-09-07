from django.test import TestCase
from ideas.models import Ideas
from utils import mongo_client

print(mongo_client)

collection_test = mongo_client.get_database('test').get_collection('test')

print(collection_test.find_one())

# Create your tests here.
class IdeasTestCases(TestCase):
    def setUp(self):
        Ideas.objects.create(name="cupcake", category="food,baked")

    def test_ideas(self):
        """Roughing in a test for the Ideas model"""
        ideais = Ideas.objects.get(name="cupcake")
        self.assertEqual(ideais.categoriesMatching(), 'A cupcake is "food,baked"')

    def test_database(self):
        if (mongo_client):
            print("Connected")
        else:
            print("Not connected")