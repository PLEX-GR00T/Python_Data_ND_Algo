"""
Name : Priyank Thakkar
Date : 15/8/2020
Info : Operations of List
"""

list1 = ['physics','chemistry',1994,3999]
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d"]

# Accessing Valuse in list
print("list1[0]:",list1[0])
print("list2[1:5]:",list2[1:5])

# Updating list
print("Value available at the index[2] : ",list1[2])
list1[2]=2002
print("New value available at the index[2]:",list1[2])
print(list1)

# Deleting list Element
del list1[2]
print("after deleting the element now list : ", list1)
