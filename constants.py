"""
    Constants
"""

# Sample file formate
SAMPLE_FORMATE = '''
Catalog file format example:
[
    {
    "sku": "IN0101",
    "name": "local item NAME",
    "category" : "beauty",
    "price": 9.99,
    "imported" : false
    },{
    "sku": "IN0102",
    "name": "imported item NAME",
    "category" : "books",
    "price": 15.29,
    "imported" : true
    }
]
'''

# Usage instructions
USAGE = '''
Usage:
    python3 sales_taxes.py [order_file]\n
Example:
    python3 sales_taxes.py data/order_1.txt
'''
# Order file format example
FORMATE_EX = '''
Order File format example:
1,IN0101
1,IN0102
2,IN0103
'''

TAX_BASIC = 10  # Basic tax on all goods except some 'specials'
TAX_IMPORT = 5  # Imported goods tax
TAX_EXEMPT = ['books', 'food', 'medical'] 
ROUND = 20