from math import ceil
import logging
from custom_exception import SalesException
from constants import ROUND

logging.getLogger(__name__)


def tax_round(tax):
    """ 
        Rounding rule for sales taxes 
    """
    return ceil(round(tax, 2) * ROUND) / ROUND



