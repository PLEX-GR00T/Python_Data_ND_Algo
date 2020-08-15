"""
Name : Priyank Thakkar
Date : 15/8/2020
Info : Insertion Operation in an Array

"""
from array import *

array3 = array('i',[11,22,33,44,55])

array3.insert(1,60) # insert(index, value)

for x in array3:
    print(x)