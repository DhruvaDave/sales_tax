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

    def add(self, quantity, sku):
        """ 
            Adding items to cart 
        """
        logging.info('Adding into cart for %s'%sku)
        entity = (sku, quantity)
        self.cart.append(entity)

    def subtotal(self):
        """ 
            Getting total price without taxes 
        """
        cart_subtotal = 0
        for ent in self.cart:
            item = StorageItem(ent[0])
            cart_subtotal += item.price * ent[1]
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
            item = StorageItem(ent[0])
            total = round((item.price + item.tax), 2)
            entities.append("{} {} at {:.2f}".format(ent[1], item.name, total))
            all_total += total
            all_taxes += item.tax
        print("\n".join(entities))
        print("Sales Taxes: {0:.2f}".format(all_taxes))
        print("Total: {0:.2f}".format(all_total))
        print("{0} HAVE A NICE DAY!!!! {0}".format("=" * 22))

