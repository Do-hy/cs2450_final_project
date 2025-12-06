# src/brands.py

class Brand:
    """
    Represents a fashion brand owned by a BrandOwner.
    A brand must be approved by an Admin before products can be added.
    """

    _id_counter = 1

    def __init__(self, name: str, owner_id: int):
        if not name:
            raise ValueError("Brand name cannot be empty.")

        self.brand_id = Brand._id_counter
        Brand._id_counter += 1

        self.name = name
        self.owner_id = owner_id
        self.approved = False  # Admin can approve this brand

    def approve(self):
        """Mark the brand as approved."""
        self.approved = True

    def __str__(self) -> str:
        status = "approved" if self.approved else "pending"
        return f"Brand(id={self.brand_id}, name={self.name}, status={status})"
