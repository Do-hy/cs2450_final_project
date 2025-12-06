# src/products.py

class Product:
    """
    Represents a product under a brand.
    Contains basic information such as name, price, and stock.
    """

    _id_counter = 1

    def __init__(self, name: str, brand_id: int, price: float, stock: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.product_id = Product._id_counter
        Product._id_counter += 1

        self.name = name
        self.brand_id = brand_id
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity: int):
        """
        Reduce available stock after purchase.
        Raises an error if quantity exceeds available stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.stock:
            raise ValueError("Not enough stock available.")

        self.stock -= quantity

    def __str__(self) -> str:
        return (
            f"Product(id={self.product_id}, name={self.name}, "
            f"price={self.price:.2f}, stock={self.stock})"
        )
