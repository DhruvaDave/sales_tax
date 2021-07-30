"""
    Stroge Items
"""

from __future__ import division
import logging
from custom_exception import SalesException
from common_lib import tax_round
from constants import TAX_BASIC, TAX_EXEMPT, TAX_IMPORT

logging.getLogger(__name__)

class StorageItem():
    """ 
        Class for storage item 
    """

    def __init__(self, ent):
        """ 
            Get object attributes by primaray key -> sku 
        """
        self.name = ent[-1]
        self.category = ent[3]
        self.price = float(ent[2])
        self.imported = ent[1]
        self.quantity = ent[0]

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

