#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import logging
from shopping_cart import ShoppingCart
from common_lib import load_order, usage
logging.basicConfig()
logging.root.setLevel(logging.INFO)

def main():
    """ Working with  """
    orders = []
    if len(sys.argv) > 1:
        orders = load_order(sys.argv[1])
    else:
        print("\nSales Taxes solution.\n")
        usage(0)
    if len(orders) < 1:
        print("ERROR: Order is empty")
        usage(1)

    cart = ShoppingCart()
    for ent in orders:
        cart.add(ent[0], ent[1])
    cart.print_receipt()
    sys.exit(0)


if __name__ == "__main__":
    main()
