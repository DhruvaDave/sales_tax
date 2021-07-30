#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import logging
from shopping_cart import ShoppingCart
from constants import TAX_VALUES
logging.basicConfig()
logging.root.setLevel(logging.INFO)


def main(input_data):
    """ 
        Main function to calculate sales tax
    """
 
    cart = ShoppingCart()
    for ent in input_data:
        quantity, imported, price, category, name = prepare_cart_data(ent)

        # Add Data in user Shopping Cart
        cart.add(quantity, imported, price, category, name)
    cart.print_receipt()
    sys.exit(0)

def prepare_cart_data(ent):
    """
        Preaparing data for Shopping Cart
    """
    imported = False
    words = ent.split(' ')
    # Spliting quantity, price and name from input
    price =  words.pop(-1)
    quantity = words.pop(0)
    words.pop(-1)

    # If item is imported then marked as True
    if "imported" in ent:
        imported = True
        words.remove('imported')

    name = ' '.join(words)
    # Defining category based on name of input item
    category = 'other'
    for key,value in TAX_VALUES.items():
        res = [i for i in value if name in i]
        if res:
            category = key
            break  
    return quantity, imported, price, category, name      


if __name__ == "__main__":
    input_data = []
    print("Enter All Your Order Details Here ...")
    while True:
        line = input()
        if line:
            input_data.append(line)
        else:
            break
    main(input_data)
