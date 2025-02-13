from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    # Step 1: Create an instance of ProductManager
    manager = ProductManager()

    # Step 2: Add multiple products
    manager.add_product(Product("Laptop", 1200, 5))
    manager.add_product(Product("Phone", 800, 3))
    manager.add_product(Product("Headphones", 150, 10))
    manager.add_product(Product("Monitor", 300, 4))

    # Step 3: Display all products
    print("\nAll Products:")
    manager.display_all_products()

    # Step 4: Display total inventory value
    print("\n" + manager.total_value())
