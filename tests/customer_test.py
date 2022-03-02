import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("The name of the Customer", 300)

    def test_customer_has_name(self):
        self.assertEqual("The name of the Customer", self.customer.name)
