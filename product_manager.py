from product import Product  # Importing the Product class

class ProductManager:
    """Manages a list of products."""
    def __init__(self):
        self.products = []  # List to store products

    def add_product(self, product):
        """Adds a new product to the list."""
        self.products.append(product)

    def display_all_products(self):
        """Displays all products in the list."""
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())

    def total_value(self):
        """Calculates and returns the total value of all products."""
        total = sum(product.price * product.quantity for product in self.products)
        return f"Total value of all products: {total:.2f}"
