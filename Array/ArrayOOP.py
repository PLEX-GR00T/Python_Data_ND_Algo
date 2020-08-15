"""
Name : Priyank Thakkar
Date : 15/8/2020
Info : All Operations of an Array

"""

from array import *

Array = array('f',[10.01,20.02,30.03,40.04,50.05])

class ArrayOOP:

    
    def traverse():
        for x in Array:
            
            print(x)

    def Access():
        for i in range(0,5):
            j=Array[i]
            print(j)
         

    def Insert(x,y):

        Array.insert(x,y)
        print("Inserted Element is here below")

        ArrayOOP.traverse()
    
    def Deletion(x):
        
        Array.remove(x)
        print("Detetion Operation is done below")

        ArrayOOP.traverse()

    def Update(x,y):

        Array[x] = y

        ArrayOOP.traverse()

obj=ArrayOOP
print("The recent Array looks like this")
obj.traverse()
print("------------------Access-------------------")
obj.Access()
print("------------------Insert-------------------")
obj.Insert(0,6.0)
print("------------------Deletion-------------------")
obj.Deletion(6.0)
print("------------------Update-------------------")
obj.Update(1,200.002)