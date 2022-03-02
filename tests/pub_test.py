import unittest
from src.pub import Pub 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The name of the Pub", 100)

    def test_pub_has_name(self):
        self.assertEqual("The name of the Pub", self. pub.name)

    def test_pub_has_a_till(self):
        self.assertEqual(100, self.pub.till)