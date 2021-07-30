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
        cart_items = [(1, False, 18.99, 'other', 'imported perfume'), (1, False, 9.75, 'medical', 'packet of headache pills'), 
                        (1, True, 27.99, 'other', 'bottle of perfume')]
        for item in cart_items:
            self.sc.add(item[0], item[1], item[2], item[3], item[4])

    def test_sc_subtotal(self):
        """ 
            Testing subtotal calculation 
        """
        self.assertEqual(self.sc.subtotal(), 56.73)


if __name__ == '__main__':
    unittest.main()
