#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import unittest
from storage_item import StorageItem


class TestStorageItem(unittest.TestCase):
    """ 
        Storage Item Class test 
    """
    def setUp(self):
        """
            Setup
        """
        self.item = StorageItem('IN0304')

    def test_local_tax(self):
        """ 
            Local items tax calculating 
        """
        si = StorageItem([1, False, 18.99, 'other', 'imported perfume'])
        self.assertEqual(si.tax, 1.9)

    def test_imported_tax(self):
        """ 
            Imported items tax calculating 
        """
        si = StorageItem([1, True, 11.25, 'food', 'box of chocolates'])
        self.assertEqual(si.tax, 0.6)

    def test_no_tax(self):
        """ 
            Check items that are exempt 
        """
        si = StorageItem([1, False, 12.49, 'book', 'book'])
        self.assertEqual(si.tax, 0)


if __name__ == '__main__':
    unittest.main()
