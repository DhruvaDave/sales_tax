#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import logging
from shopping_cart import ShoppingCart
from common_lib import load_order, usage
from constants import TAX_EXEMPT, TAX_VALUES
logging.basicConfig()
logging.root.setLevel(logging.INFO)

def main(input_data):
    """ 
        Main function to calculate sales tax
    """
 
    cart = ShoppingCart()
    for ent in input_data:
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
        # Add Data in user Shopping Cart
        cart.add(quantity, imported, price, category, name)
    cart.print_receipt()
    sys.exit(0)


if __name__ == "__main__":
    input_data = []
    print("Enter All Your Orders Here ...")
    while True:
        line = input()
        if line:
            input_data.append(line)
        else:
            break
    main(input_data)
