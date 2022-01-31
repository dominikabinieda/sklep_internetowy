from django.test import TestCase
import unittest
from sklep.models import Product, Category


# Create your tests here.

class ProduktyTest(unittest.TestCase):

    def setUp(self):
        Product(name='naszyjnik', price=125.00)

    def test_product_price(self):
        self.assertEqual(Product.price, 125.00)

    def test_product_name(self):
        self.assertEqual(Product.name, 'naszyjnik')



if __name__ == "__main__":
    unittest.main()