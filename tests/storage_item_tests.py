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
        si = StorageItem('IN0302')
        self.assertEqual(si.tax, 1.9)

    def test_imported_tax(self):
        """ 
            Imported items tax calculating 
        """
        si = StorageItem('IN0304')
        self.assertEqual(si.tax, 0.6)

    def test_no_tax(self):
        """ 
            Check items that are exempt 
        """
        si = StorageItem('IN0101')
        self.assertEqual(si.tax, 0)


if __name__ == '__main__':
    unittest.main()
