from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="pizza", Price=0.01, Inventory=1)
        self.assertEqual(str(item), "pizza : 0.01")