import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("The name of the Drink", 3)
        

    def test_drink_has_name(self):
        self.assertEqual("The name of the Drink", self.drink.name)

    # def test_pub_has_a_till(self):
    #     self.assertEqual(100, self.pub.till)

    # def test_pub_has_drinks(self):
    #     self.assertEqual(["wine", "beer", "guiness"], self.pub.drinks)

    # def test_can_change_name(self):
    #     self.pub.name = "The dancing Pony"
    #     self.assertEqual("The dancing Pony", self.pub.name)