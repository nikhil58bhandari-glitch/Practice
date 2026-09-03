import numpy as np

    # * Join & Split Functions in NumPy ->
 # join->
var = np.array([1,2,3,4,5,6,9])
var2 = np.array([5,6,7,89,4,5])

ar = np.concatenate((var, var2))
print(ar)
print()

var3 = np.array([[23,45,64,3],[42,5,6,43]])
print(var3)
var4 = np.array([[3,4,6,7],[5,6,7,89]])
print(var4)
print()
ar1 = np.concatenate((var3,var4),axis = 0)
print(ar1)
print()

v1 = np.array([2,4,6,7])
v2 = np.array([2,3,4,6])
a_new = np.stack((v1,v2),axis = 1)
print(a_new)
print()

a_new1 = np.hstack((v1,v2))    #  rows
print(a_new1)
print()

a_new2 = np.vstack((v1,v2))   # colums
print(a_new2)
print()

a_new3 = np.dstack((v1,v2))   # height
print(a_new3)
print()

 # Split->
var = np.array([3,4,6,7,6,3])
print(var)
ar = np.array_split(var,4)
print(ar)
print(ar[0])

x = np.array([[4,3,5],[9,8,7],[0,9,7]])
print(x)
ar1 = np.array_split(x,4)
print(ar1)
print()

ar2 = np.array_split(x,4,axis=1)
print(ar2)
print()
