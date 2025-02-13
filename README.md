Online Sales Analysis

Project Overview:
The Online Sales Analysis project is a simple Python-based shopping cart system. It allows users to:

Manage a list of available products.
Add products to a shopping cart.
Calculate the total price of selected items.
Randomly select products to be added to the cart.
This project follows object-oriented programming (OOP) principles and provides a modular and extensible structure.

Project Structure:

product.py - Defines the Product class.
product_manager.py - Manages product inventory (add, remove, display).
cart.py - Shopping cart functionalities.
main.py - Entry point of the application.
.gitignore - Excludes sensitive files (config.json, screenshots).
README.md - Project documentation.
config.json (ignored) - Example API key storage (not tracked in Git).
Classes & Functionalities:

1️⃣ Product (product.py)
Represents an individual product with the following attributes:

name - The name of the product.
price - The price of the product.
quantity - The number of units available.
Example Usage:
product = Product("Laptop", 1200, 5)
print(product.display_info()) # Output: Product: Laptop, Price: 1200, Quantity: 5

2️⃣ ProductManager (product_manager.py)
Manages the inventory of products.

Features:
✔ Add a product
✔ Remove a product by name
✔ Display all available products
✔ Calculate the total inventory value

Example Usage:
manager = ProductManager()
manager.add_product(Product("Phone", 800, 3))
manager.display_all_products()

3️⃣ Cart (cart.py)
Handles the shopping cart, allowing users to add and view products.

Features:
✔ Add a product to the cart
✔ Display cart contents
✔ Calculate the total cart value

Example Usage:
cart = Cart()
cart.add_to_cart(Product("Monitor", 300, 2), 2)
cart.display_cart()
print(cart.calculate_total())

4️⃣ Main Script (main.py)
Orchestrates the entire program.

Steps Performed:

Creates a ProductManager instance.
Adds products to the inventory.
Creates a Cart instance.
Randomly selects 3 products and adds them to the cart.
Displays the cart contents and total price.
Example Usage:
python main.py

Running the Project:

1️⃣ Clone the Repository:
git clone https://github.com/wolfnote/online_sales_analysis.git

2️⃣ Run the Main Script:
python main.py

Security Measures:

The project ignores config.json (which contains sensitive API keys).
Screenshots (.png, .jpg, etc.) are excluded to keep the repository clean.
See the .gitignore file for excluded items.
Future Improvements:
✅ Implement a database to store products.
✅ Add a Graphical User Interface (GUI).
✅ Improve product filtering and search functionality.

Author:
👨‍💻 Zoran Borisavljevic
📧 zoranboris@gmail.com
🔗 https://github.com/wolfnote
