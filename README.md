# Sales Taxes problem solution

The Problem
---

Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical 
products that are exempt. Import duty is an additional sales tax applicable on all imported goods 
at a rate of 5%, with no exemptions. 
  
When I purchase items I receive a receipt which lists the name of all the items and their price 
(including tax), finishing with the total cost of the items, and the total amounts of sales taxes 
paid.  The rounding rules for sales tax are that for a tax rate of n%, a shelf price of p contains 
(np/100 rounded up to the nearest 0.05) amount of sales tax. 
  
Write an application that prints out the receipt details for these shopping baskets... 
  
Input: 
  
Input 1: 

1 book at 12.49 

1 music CD at 14.99 

1 chocolate bar at 0.85 
  

Input 2: 

1 imported box of chocolates at 10.00 

1 imported bottle of perfume at 47.50 
  

Input 3: 

1 imported bottle of perfume at 27.99 

1 bottle of perfume at 18.99 

1 packet of headache pills at 9.75 

1 box of imported chocolates at 11.25 
  
Output: 
  
Output 1: 

1 book : 12.49 

1 music CD: 16.49 

1 chocolate bar: 0.85 

Sales Taxes: 1.50 

Total: 29.83 
  
Output 2: 

1 imported box of chocolates: 10.50 

1 imported bottle of perfume: 54.65 

Sales Taxes: 7.65 

Total: 65.15 
  
Output 3: 

1 imported bottle of perfume: 32.19 

1 bottle of perfume: 20.89 

1 packet of headache pills: 9.75 

1 imported box of chocolates: 11.85 

Sales Taxes: 6.70 

Total: 74.68 

========== 


Design Aspect
---
As this problem is quite simple, I have decided to use two classes one for StorageItem and one for Shopping Cart.
StorageItem will calculate taxes and all necessary information for particular item. Cart will add add items in orders.

I have used static JSON format file (data/available_items.json) with available items which will be easy to modify in future.

___

Usage
---
Only standard library was used, so to run this solution, you need only **Python 3**.

Go to directory where *sales_tax_demo.py* stored.

To run solution, type ```python3 sales_taxes.py <order items>```, for example:

To test input:
 
```python3 sales_tax_demo.py```

```1 book at 12.49 ```

```1 music CD at 14.99 ```

```1 chocolate bar at 0.85 ```


Unit Test
---

I have created tests dictory to cover unit tests for all files.

To run tests, type ```python3 tests/file_name.py```.Add ```-v``` argument if you want verbosity.

ShoppingCart unit test:  ```python3 tests/shopping_cart_tests.py``` 

StorageItem unit test:  ```python3 tests/storage_item_tests.py``` 

Common unit test:  ```python3 tests/common_lib_tests.py``` 



