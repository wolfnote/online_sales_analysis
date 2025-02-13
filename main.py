from product import Product
from product_manager import ProductManager
from cart import Cart  # Import the Cart class
import random  # For randomly selecting products

if __name__ == "__main__":
    # Step 1: Create an instance of ProductManager and add products
    manager = ProductManager()
    
    manager.add_product(Product("Laptop", 1200, 5))
    manager.add_product(Product("Phone", 800, 3))
    manager.add_product(Product("Headphones", 150, 10))
    manager.add_product(Product("Monitor", 300, 4))
    manager.add_product(Product("Keyboard", 200, 6))

    # Step 2: Display all available products
    print("\nAvailable Products:")
    manager.display_all_products()

    # Step 3: Create a Cart instance
    cart = Cart()

    # Step 4: Randomly select three products from the available product list
    available_products = manager.products
    if len(available_products) >= 3:
        selected_products = random.sample(available_products, 3)  # Select 3 random products

        # Add selected products to the cart
        print("\nAdding products to the cart...")
        for product in selected_products:
            cart.add_to_cart(product, random.randint(1, 3))  # Random quantity between 1 and 3

    # Step 5: Display cart contents
    cart.display_cart()

    # Step 6: Display total cart value
    print("\n" + cart.calculate_total())
