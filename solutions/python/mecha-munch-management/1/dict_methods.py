"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        if current_cart.get(item) != None:
            current_cart[item] = current_cart.get(item) + 1
        else:
            current_cart[item] = 1
    
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    shopping_cart = {}

    for note in notes:
        if shopping_cart.get(note) != None:
            shopping_cart[note] = shopping_cart.get(note) + 1
        else:
            shopping_cart[note] = 1

    return shopping_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    dict = {}
    
    for item in sorted(cart, reverse=True):
        dict[item] = [
            cart[item],
            aisle_mapping[item][0],
            aisle_mapping[item][1]
        ]

    return dict

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    dict = store_inventory.copy()

    for item in fulfillment_cart:
        if store_inventory.get(item) != None:
            fulfillment_item_count = fulfillment_cart[item][0]
            store_inventory_item_count = store_inventory[item][0]

            diff = store_inventory_item_count - fulfillment_item_count

            if diff > 0:
                dict[item] = [diff, fulfillment_cart[item][1], fulfillment_cart[item][2]]
            else:
                dict[item] = ['Out of Stock', fulfillment_cart[item][1], fulfillment_cart[item][2]]

    return dict
