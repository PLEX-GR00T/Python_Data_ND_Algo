"""
Name : Priyank Thakkar
Date : 15/8/2020
Info : Traverse in 2D Array
"""
import sys
from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for x in T:
    for y in x:
        print(y, end = " ")
    print()