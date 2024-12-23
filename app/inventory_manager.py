# Placeholder for future inventory management logic
# For example, functions to add, remove, and update inventory could go here.
inventory = {}


# baseline functions for initial testing
def add_item(item_name, quantity):
    """Add or update an item in the inventory."""
    inventory[item_name] = inventory.get(item_name, 0) + quantity

def remove_item(item_name, quantity):
    """Remove an item or reduce its quantity."""
    if item_name in inventory:
        inventory[item_name] -= quantity
        if inventory[item_name] <= 0:
            del inventory[item_name]
