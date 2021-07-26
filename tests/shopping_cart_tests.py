#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import unittest
from shopping_cart import ShoppingCart



class TestShoppintCart(unittest.TestCase):
    """ 
        Shopping Cart testing 
    """
    def setUp(self):
        """
            Unit test Setup
        """
        self.sc = ShoppingCart()
        cart_items = [(1, 'IN0302'), (1, 'IN0303'), (1, 'IN0301')]
        for item in cart_items:
            self.sc.add(item[0], item[1])

    def test_sc_subtotal(self):
        """ 
            Testing subtotal calculation 
        """
        self.assertEqual(self.sc.subtotal(), 56.73)


if __name__ == '__main__':
    unittest.main()
