
import unittest
from common_lib import tax_round

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

