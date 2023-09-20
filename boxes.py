"""
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping.
Write a Python program named boxes.py that asks the user for two integers:
1. the number of manufactured items
2. the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number.
Note that the last box may be packed with fewer items than the other boxes.
"""
import math

items = int(input("Enter the number of items: "))
itemsPerBox = int(input("Enter the number of items per box: "))
totalBoxes = math.ceil((items / itemsPerBox))

print(f'For {items} items, packing {itemsPerBox} items in each box, you will need {totalBoxes} boxes.')