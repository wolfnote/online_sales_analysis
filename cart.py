from product import Product  # Import the Product class
import random  # For randomly selecting products

class Cart:
    """Class for managing a shopping cart."""
    
    def __init__(self):
        self.cart_items = []  # List to store products in the cart

    def add_to_cart(self, product, quantity):
        """Adds a product to the cart with the specified quantity."""
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
        
        # Check if the product already exists in the cart
        for item in self.cart_items:
            if item["product"].name == product.name:
                item["quantity"] += quantity
                print(f"Added {quantity} more of {product.name} to the cart.")
                return
        
        # If the product is not in the cart, add it
        self.cart_items.append({"product": product, "quantity": quantity})
        print(f"Added {product.name} ({quantity} pcs) to the cart.")

    def calculate_total(self):
        """Calculates and returns the total cart value."""
        total = sum(item["product"].price * item["quantity"] for item in self.cart_items)
        return f"Total cart value: {total:.2f} RSD"

    def display_cart(self):
        """Displays all products in the cart."""
        if not self.cart_items:
            print("The cart is empty.")
        else:
            print("\nCart Contents:")
            for item in self.cart_items:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.name} - Price: {product.price} RSD, Quantity: {quantity}")
