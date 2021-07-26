"""
    Stroge Items
"""

from __future__ import division
import logging
from custom_exception import SalesException
from common_lib import load_all_items, tax_round
from constants import TAX_BASIC, TAX_EXEMPT, TAX_IMPORT

logging.getLogger(__name__)

class StorageItem():
    """ 
        Class for storage item 
    """
    all_items = load_all_items()

    def __init__(self, sku):
        """ 
            Get object attributes by primaray key -> sku 
        """
        item = list(filter(lambda x: x.get('sku') == sku, StorageItem.all_items))
        logging.debug('Storage Item: %s' %item)
        if len(item) < 1:
            logging.debug('SKU not found in available items %s'%(sku))
            raise SalesException('SKU Not Fonud.')
        self.name = item[0]['name']
        self.category = item[0]['category']
        self.price = item[0]['price']
        self.imported = item[0]['imported']
        self.tax = self.calc_tax()

    def calc_tax(self):
        """ 
            Calculating tax 
        """
        logging.info("calcultating tax")
        tax = 0
        total_tax = 0
        result_tax = 0
        if self.category not in TAX_EXEMPT:
            tax += TAX_BASIC
        if self.imported:
            tax += TAX_IMPORT
        
        # Convert tax to percents
        if tax > 0:
            total_tax = self.price * (tax/100)
            result_tax = tax_round(total_tax)
        return result_tax

