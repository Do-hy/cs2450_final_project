# tests/test_orders.py

import unittest
from src.orders import Order, OrderItem, OrderStatus


class TestOrder(unittest.TestCase):
    def test_order_total(self):
        order = Order(customer_id=1)
        order.add_item(OrderItem(1, "A", 10.0, 2))  # 20
        order.add_item(OrderItem(2, "B", 5.0, 3))   # 15
        self.assertAlmostEqual(order.total_amount, 35.0)

    def test_mark_paid_changes_status(self):
        order = Order(customer_id=1)
        order.add_item(OrderItem(1, "A", 10.0, 1))
        order.mark_paid()
        self.assertEqual(order.status, OrderStatus.PAID)


if __name__ == "__main__":
    unittest.main()
