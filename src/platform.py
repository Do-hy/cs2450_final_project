# src/platform.py

from typing import Dict, List, Optional

from .users import User, Customer, BrandOwner, Admin
from .brands import Brand
from .products import Product
from .orders import Order, OrderItem


class PlatformManager:
    """
    Singleton class managing all platform operations.
    Stores users, brands, products, and orders in memory.
    """

    _instance: Optional["PlatformManager"] = None

    def __init__(self):
        if PlatformManager._instance is not None:
            raise RuntimeError("Use get_instance() instead of creating directly.")

        # In-memory storage
        self.users: Dict[int, User] = {}
        self.brands: Dict[int, Brand] = {}
        self.products: Dict[int, Product] = {}
        self.orders: Dict[int, Order] = {}

    @classmethod
    def get_instance(cls) -> "PlatformManager":
        """Return the single instance of the platform manager."""
        if cls._instance is None:
            cls._instance = PlatformManager()
        return cls._instance

    # -----------------------------------------
    # User Management
    # -----------------------------------------

    def register_customer(self, name: str, email: str) -> Customer:
        """Register a new customer."""
        customer = Customer(name, email)
        self.users[customer.user_id] = customer
        return customer

    def register_brand_owner(self, name: str, email: str) -> BrandOwner:
        """Register a new brand owner."""
        owner = BrandOwner(name, email)
        self.users[owner.user_id] = owner
        return owner

    def create_admin(self, name: str, email: str) -> Admin:
        """Create a new admin."""
        admin = Admin(name, email)
        self.users[admin.user_id] = admin
        return admin

    # -----------------------------------------
    # Brand Management
    # -----------------------------------------

    def request_brand(self, owner_id: int, brand_name: str) -> Brand:
        """Brand owner requests approval for a new brand."""
        if owner_id not in self.users or not isinstance(self.users[owner_id], BrandOwner):
            raise ValueError("Invalid brand owner ID.")

        brand = Brand(brand_name, owner_id)
        self.brands[brand.brand_id] = brand

        owner: BrandOwner = self.users[owner_id]  # type: ignore
        owner.brand_id = brand.brand_id
        return brand

    def approve_brand(self, admin_id: int, brand_id: int):
        """Admin approves a brand."""
        if admin_id not in self.users or not isinstance(self.users[admin_id], Admin):
            raise ValueError("Only admin can approve brands.")

        brand = self.brands.get(brand_id)
        if brand is None:
            raise ValueError("Brand not found.")

        brand.approve()

    # -----------------------------------------
    # Product Management
    # -----------------------------------------

    def add_product(self, owner_id: int, name: str, price: float, stock: int) -> Product:
        """Brand owner adds a product under an approved brand."""
        if owner_id not in self.users or not isinstance(self.users[owner_id], BrandOwner):
            raise ValueError("Only brand owners can add products.")

        owner: BrandOwner = self.users[owner_id]  # type: ignore
        if owner.brand_id is None:
            raise ValueError("Brand owner does not have an associated brand.")

        brand = self.brands.get(owner.brand_id)
        if brand is None or not brand.approved:
            raise ValueError("Brand must be approved before adding products.")

        product = Product(name, brand.brand_id, price, stock)
        self.products[product.product_id] = product
        return product

    def list_products(self) -> List[Product]:
        """Return a list of all products."""
        return list(self.products.values())

    # -----------------------------------------
    # Order Management
    # -----------------------------------------

    def create_order(self, customer_id: int, items: Dict[int, int]) -> Order:
        """Create and process an order for a customer."""
        if customer_id not in self.users or not isinstance(self.users[customer_id], Customer):
            raise ValueError("Invalid customer ID.")

        order = Order(customer_id)

        for product_id, quantity in items.items():
            product = self.products.get(product_id)
            if product is None:
                raise ValueError(f"Product {product_id} not found.")

            product.reduce_stock(quantity)

            line_item = OrderItem(
                product_id=product.product_id,
                product_name=product.name,
                unit_price=product.price,
                quantity=quantity,
            )
            order.add_item(line_item)

        order.mark_paid()
        self.orders[order.order_id] = order
        return order

    def list_orders_for_customer(self, customer_id: int) -> List[Order]:
        """Return all orders placed by a specific customer."""
        return [o for o in self.orders.values() if o.customer_id == customer_id]
