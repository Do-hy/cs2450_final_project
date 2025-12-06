# src/orders.py

from typing import List
from enum import Enum


class OrderStatus(str, Enum):
    """Represents the current status of the order."""

    PENDING = "PENDING"
    PAID = "PAID"
    SHIPPED = "SHIPPED"


class OrderItem:
    """
    Represents one line item in an order.
    Stores product information and quantity.
    """

    def __init__(self, product_id: int, product_name: str, unit_price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if unit_price < 0:
            raise ValueError("Unit price cannot be negative.")

        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    @property
    def line_total(self) -> float:
        """Calculate total price for this item."""
        return self.unit_price * self.quantity

    def __str__(self) -> str:
        return f"{self.product_name} (x{self.quantity}) - {self.line_total:.2f}"


class Order:
    """Represents a customer's order containing multiple items."""

    _id_counter = 1

    def __init__(self, customer_id: int):
        self.order_id = Order._id_counter
        Order._id_counter += 1

        self.customer_id = customer_id
        self.items: List[OrderItem] = []
        self.status: OrderStatus = OrderStatus.PENDING

    def add_item(self, item: OrderItem):
        """Add an item to the order."""
        self.items.append(item)

    @property
    def total_amount(self) -> float:
        """Return total cost of the order."""
        return sum(item.line_total for item in self.items)

    def mark_paid(self):
        """Set order status to PAID."""
        if not self.items:
            raise ValueError("Order must have items before payment.")
        self.status = OrderStatus.PAID

    def __str__(self) -> str:
        items_str = ", ".join(str(item) for item in self.items)
        return (
            f"Order(id={self.order_id}, customer_id={self.customer_id}, "
            f"status={self.status}, total={self.total_amount:.2f}, "
            f"items=[{items_str}])"
        )
