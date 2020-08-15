"""
Name : Priyank Thakkar
Date : 15/8/2020
Info : Tuples operation
"""

# Initialize Tuple
tup1 = ('Physics','chemistry', 1997,2900)
tup2 = (1,2,4,4,5)
tup3 = ("a","b","c","d")

# Empty tuple
tup=()

# Tuple with single value
tup4=(60,)

# Accessing Values
print("tup1[0]:", tup1[0])
print("tup2[1:5]:", tup2[1:5])

# Updating Tuples
""" Updating tuples is not at all possible"""
tup5 = tup1+tup2+tup3
print(tup5)


# Deleting Tuple
del tup2
print("------------------Deleting error messeage ---------------")
print("After deleting tup2",tup2)
