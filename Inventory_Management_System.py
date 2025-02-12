import json
import os

INVENTORY_FILE = "inventory.json"

def load_inventory():
    """Loads inventory data from a JSON file."""
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_inventory(inventory):
    """Saves inventory data to a JSON file."""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=24)

def add_item(inventory):
    """Adds a new item to the inventory."""
    name = input("Enter item name: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"Item '{name}' added successfully.")
    except ValueError:
        print("Invalid input. Quantity and price must be numeric.")

def update_item(inventory):
    """Updates the quantity or price of an existing item."""
    name = input("Enter item name to update: ")
    if name in inventory:
        try:
            new_quantity = input("Enter new quantity : ")
            new_price = input("Enter new price : ")

            if new_quantity:
                inventory[name]["quantity"] = int(new_quantity)
            if new_price:
                inventory[name]["price"] = float(new_price)
            print(f"Item '{name}' updated successfully.")
        except ValueError:
            print("Invalid input. Quantity and price must be numeric.")
    else:
        print(f"Item '{name}' not found in inventory.")

def view_inventory(inventory):
    """Displays the current inventory."""
    if inventory:
        print("Inventory:")
        for name, details in inventory.items():
            print(f"- {name}: Quantity: {details['quantity']}, Price: {details['price']}")
    else:
        print("Inventory is empty.")

def search_item(inventory):
    """Searches for an item by name."""
    name = input("Enter item name to search: ")
    if name in inventory:
        details = inventory[name]
        print(f"Item '{name}' found: Quantity: {details['quantity']}, Price: {details['price']}")
    else:
        print(f"Item '{name}' not found in inventory.")

def main():
    """Main function to run the inventory management system."""
    inventory = load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Search Item")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            update_item(inventory)
        elif choice == "3":
            view_inventory(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
