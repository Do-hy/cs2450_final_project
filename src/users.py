# src/users.py

from abc import ABC, abstractmethod
from typing import Optional


class User(ABC):
    """
    Abstract base class for all user types in the system.
    Each user has a unique ID, name, and email address.
    """

    _id_counter = 1

    def __init__(self, name: str, email: str):
        if not name:
            raise ValueError("Name cannot be empty.")
        if "@" not in email:
            raise ValueError("Invalid email address.")

        self.user_id = User._id_counter
        User._id_counter += 1

        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self) -> str:
        """Return the role of the user (Customer, BrandOwner, Admin)."""
        pass

    def __str__(self) -> str:
        return f"{self.get_role()}(id={self.user_id}, name={self.name})"


class Customer(User):
    """Represents a customer who can browse products and place orders."""

    def get_role(self) -> str:
        return "Customer"


class BrandOwner(User):
    """Represents a brand owner who can manage a brand and add products."""

    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.brand_id: Optional[int] = None  # Assigned after brand creation

    def get_role(self) -> str:
        return "BrandOwner"


class Admin(User):
    """Represents an admin who can approve brands and oversee the platform."""

    def get_role(self) -> str:
        return "Admin"
