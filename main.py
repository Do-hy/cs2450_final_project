# main.py

from src.platform import PlatformManager


def seed_data(platform: PlatformManager):
    """
    Create default users and brand data for demonstration purposes.
    """
    admin = platform.create_admin("AdminUser", "admin@example.com")
    owner = platform.register_brand_owner("Brand Owner", "owner@example.com")
    customer = platform.register_customer("Customer A", "customer@example.com")

    brand = platform.request_brand(owner.user_id, "Minimalist Studio")
    platform.approve_brand(admin.user_id, brand.brand_id)

    platform.add_product(owner.user_id, "White T-shirt", 25.0, 10)
    platform.add_product(owner.user_id, "Black Jeans", 60.0, 5)

    return admin, owner, customer


def show_products(platform: PlatformManager):
    """Display all available products."""
    print("\n=== Product List === (Please use product ID and quantity)")
    for p in platform.list_products():
        print(f"{p.product_id}. {p.name} - ${p.price:.2f} (stock: {p.stock})")


def customer_flow(platform: PlatformManager, customer_id: int):
    """
    Simple console flow for customers to place orders.
    """
    while True:
        show_products(platform)
        print("\nEnter product id and quantity to order (or 'q' to quit):")
        user_input = input("> ").strip()

        if user_input.lower() == "q":
            break

        try:
            product_id_str, qty_str = user_input.split()
            product_id = int(product_id_str)
            quantity = int(qty_str)
        except ValueError:
            print("Invalid format. Please use: <product_id> <quantity>")
            continue

        try:
            order = platform.create_order(customer_id, {product_id: quantity})
            print("\nOrder created successfully:")
            print(order)

        except Exception as e:
            print(f"Error: {e}")


def main():
    platform = PlatformManager.get_instance()
    _, _, customer = seed_data(platform)

    print("Welcome to the Multi-Brand Fashion Platform (console demo)")
    customer_flow(platform, customer.user_id)

    print("\nYour order history:")
    for order in platform.list_orders_for_customer(customer.user_id):
        print(order)


if __name__ == "__main__":
    main()
