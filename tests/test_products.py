# tests/test_products.py

import unittest
from src.products import Product


class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        p = Product("Shirt", brand_id=1, price=20.0, stock=5)
        self.assertEqual(p.name, "Shirt")
        self.assertEqual(p.stock, 5)

    def test_negative_price_raises(self):
        with self.assertRaises(ValueError):
            Product("Bad", brand_id=1, price=-1.0, stock=1)


if __name__ == "__main__":
    unittest.main()
