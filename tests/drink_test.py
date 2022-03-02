import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("The name of the Drink", 3)
        

    def test_drink_has_name(self):
        self.assertEqual("The name of the Drink", self.drink.name)

    def test_drink_has_a_price(self):
        self.assertEqual(3, self.drink.price)
