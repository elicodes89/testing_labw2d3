import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("The name of the Customer", 100)

    def test_customer_has_name(self):
        self.assertEqual("The name of the Customer", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_can_afford_drink(self):
        self.customer.can_afford_drink(3)
        self.assertEqual(True, self.customer.can_afford_drink(3))

    def test_remove_from_wallet(self):
        self.customer.remove_from_wallet(3)
        self.assertEqual(97, self.customer.wallet)

    # def test_can_buy_drink(self):
    #     customer_1 = Customer("Bill", 50)
    #     customer_2 = Customer("Rosa", 1)
    #     drink_1 = Drink("beer", 4)
    #     drink_2 = Drink("wine", 6)
    #     self.customer.can_afford_drink(drink_1)

    
