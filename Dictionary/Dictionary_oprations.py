"""
Name : Priyank Thakkar
Date : 15/8/2020
Info : Dictionary Operations
"""

# Accesing Values in Dictionary
dict = {'Name' : 'Priyank', 'Age' : 7, 'Class' : 'First'}
print("dict['Name'] : ",dict['Name'])
print("dict['Age']:", dict['Age'])

# Aceesing the element with the key which is not present in the dict we get and error

# Updating Values
dict['Age'] = 9
dict['School'] = " Utkarsh Vidyalay, Gujarati Medium "
print("dict['School'] : ",dict['School'])
print("dict['Age']:", dict['Age'])

# Deleting Dictionary
del dict['Name'] # remove entry with the key name 'Name'
dict.clear()     # remove all entries in dict
del dict        # delete entire dictionry

"""
NOTE : Properties of Dictionary Keys
1) More than one entry per key not allowed.
    which means no duplicate key is allowed.
    when duplicate keys encountered during assignmaent,
    the last assignment wins
    For Example : 
"""
dict1 = {'Name' : 'Piyu', 'Name' : 'Priyank'}
print("dict1['Name']",dict1['Name'])

"""
2) Keys must be immutable. 
    Which means you can use stings, numbers or tuples as dictionary keys
    but something like['key'] is not allowed.
"""
dict2 = {['Name']: 'Zara', 'Age': 7}
print ("dict2['Name']: ", dict2['Name'])