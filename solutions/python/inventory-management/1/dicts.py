"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventories = dict()

    for item in items:
        if inventories.get(item) is not None:
            counter = inventories.get(item) + 1
            inventories[item] = counter
        else:
            inventories[item] = 1

    return inventories

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """

    for item in items:
        if inventory.get(item) is not None:
            counter = inventory.get(item) + 1
            inventory[item] = counter
        else:
            inventory[item] = 1

    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    for item in items:
        if inventory.get(item) is not None and inventory.get(item) != 0:
            counter = inventory.get(item) - 1
            inventory[item] = counter
        
    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """

    if inventory.get(item) is not None:
        inventory.pop(item)

    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    available_items = []

    for key, value in inventory.items():
        if value > 0:
            available_items.append((key, value))

    return available_items
