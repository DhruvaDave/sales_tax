
import unittest
from common_lib import tax_round, load_order

class TestCommonMethods(unittest.TestCase):
    """ 
        Checking Common functions 
    """
    def test_tax_round(self):
        """ 
            Checking if tax rounding works fine 
        """
        taxes = [2.04, 4.08, 8.16, 9.99, 16.32, 32.64, 512.24]
        rtaxes = [2.05, 4.1, 8.2, 10.0, 16.35, 32.65, 512.25]
        for i in taxes:
            self.assertEqual(tax_round(i), rtaxes[taxes.index(i)])

    def test_load_order_success(self):
        """ 
            Simple order loading success 
        """
        order = "data/test_order.txt"
        lo =load_order(order)
        self.assertEqual(len(lo), 9)

    def test_load_order_failed(self):
        """ 
            Simple order loading fail 
        """
        order = "data/test_order_fail.txt"
        lo =load_order(order)
        self.assertNotEqual(len(lo), 9)
