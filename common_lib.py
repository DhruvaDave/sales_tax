import os 
import json
from math import ceil
import logging
import sys
from custom_exception import SalesException
from constants import SAMPLE_FORMATE, USAGE, FORMATE_EX, ROUND

logging.getLogger(__name__)


def usage(ec):
    """ 
        Exit 0 for successful usage
        Exit 1 if any error occurs in usage   
    """
    print(USAGE)
    sys.exit(ec)


def orderfile_error(msg, line, cont):
    """ 
        Returns error details if order is wrong 
    """
    print(msg)
    print("Wrong line: {}, Content: '{}'".format(line, cont.strip('\n')))
    print(FORMATE_EX)
    sys.exit(1)



def load_order(order_file):
    """ 
        Loading order file 
    """
    orderlist = []
    with open(order_file, 'r') as order:
        data = order.readlines()
    for item in data:
        line = data.index(item) + 1
        try:
            quantity, sku = item.strip('\n').split(',')  # Remove newlines
        except ValueError:
            orderfile_error("ERROR: Order file format is broken.", line, item)
        quantity = int(quantity.strip(' '))  # Converting to int and stripping out whitespaces
        if quantity < 1:
            orderfile_error("ERROR: Quantity cannot be less than 1.", line, item)  # Returning an error and exitting
        sku = sku.strip(' ')  # Stripping out whitespaces
        entity = (quantity, sku)
        orderlist.append(entity)
    return orderlist

def check_item(catalog):
    """ 
        Checking if item file has all needed keys 
    """
    keys = ['sku', 'name', 'category', 'price', 'imported']
    for item in catalog:
        if not len([x for x in keys if x in item]) == len(keys):
            print(SAMPLE_FORMATE)
            raise SalesException(message="ERROR: Wrong input")
            
    return True

def tax_round(tax):
    """ 
        Rounding rule for sales taxes 
    """
    return ceil(round(tax, 2) * ROUND) / ROUND


def load_all_items():
    """ 
        Loading all items from json list. 
    """
    logging.info('Loading all items from list.')
    with open(os.path.join('data', 'available_items.json'), 'r') as avail_item:
        items = json.load(avail_item)
    logging.info('Calling check item')
    if check_item(items):
        return items
