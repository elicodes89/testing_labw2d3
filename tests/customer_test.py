import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("The name of the Customer", 100)

    def test_customer_has_name(self):
        self.assertEqual("The name of the Customer", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    
