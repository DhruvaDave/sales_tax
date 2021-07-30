"""
    My Shopping Cart
"""

import logging
from storage_item import StorageItem

class ShoppingCart():
    """ 
        Shopping Cart 
    """
    def __init__(self):
        self.cart = []

    def add(self, quantity, imported, price, category, name):
        """ 
            Adding items to cart 
        """
        logging.info('Adding into cart for %s'%quantity)
        entity = (quantity, imported, price, category, name)
        self.cart.append(entity)

    def subtotal(self):
        """ 
            Getting total price without taxes 
        """
        cart_subtotal = 0
        for ent in self.cart:
            item = StorageItem(ent)
            cart_subtotal += item.price
        return cart_subtotal

    def print_receipt(self):
        """ 
            Printing receipt 
        """
        print("{0} Ordered Items {0}".format("=" * 25))
        entities = []
        all_total = 0
        all_taxes = 0
        for ent in self.cart:
            item = StorageItem(ent)
            total = round((item.price + item.tax), 2)
            entities.append("{} {} at {:.2f}".format(item.quantity, item.name, total))
            all_total += total
            all_taxes += item.tax
        print("\n".join(entities))
        print("Sales Taxes: {0:.2f}".format(all_taxes))
        print("Total: {0:.2f}".format(all_total))
        print("{0} HAVE A NICE DAY!!!! {0}".format("=" * 22))

