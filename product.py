class Product:
    """Represents a product with name, price, and quantity."""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Returns product details as a formatted string."""
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
