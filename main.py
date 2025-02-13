from product import Product
from product_manager import ProductManager
from cart import Cart  # Import the Cart class
import random  # For randomly selecting products

if __name__ == "__main__":
    # Step 1: Create an instance of ProductManager and add products
    manager = ProductManager()
    
    manager.add_product(Product("Gaming Laptop", 1500, 4))  # Changed name and quantity
    manager.add_product(Product("Smartphone", 900, 5))  # Changed name and quantity
    manager.add_product(Product("Wireless Headphones", 200, 8))  # Changed name and quantity
    manager.add_product(Product("4K Monitor", 400, 3))  # Changed name and quantity
    manager.add_product(Product("Mechanical Keyboard", 250, 7))  # Changed name and quantity

    # Step 2: Create a Cart instance
    cart = Cart()

    # Step 3: Randomly select three products from the available product list
    available_products = manager.products
    if len(available_products) >= 3:
        selected_products = random.sample(available_products, 3)  # Select 3 random products

        # Add selected products to the cart
        print("\nAdding products to the cart...")
        for product in selected_products:
            cart.add_to_cart(product, random.randint(1, 3))  # Random quantity between 1 and 3

    # Step 4: Display cart contents
    cart.display_cart()

    # Step 5: Display total cart value
    print("\n" + cart.calculate_total())
