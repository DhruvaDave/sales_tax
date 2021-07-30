"""
    Constants
"""

# Usage instructions
USAGE = '''
Usage:
    python3 \n
    <order item input>
    <order item input>
Example:
    python3 sales_taxes.py
    1 book at 12.49
    1 music CD at 14.99
    1 chocolate bar at 0.85
'''


TAX_BASIC = 10  # Basic tax on all goods except some 'specials'
TAX_IMPORT = 5  # Imported goods tax
TAX_EXEMPT = ['book', 'food', 'medical'] # Exempt Tax Products
TAX_VALUES = {'book': ['book'], 'food': ['box of chocolates', 'chocolate bar'], 'medical': ['packet of headache pills']}
ROUND = 20