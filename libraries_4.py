import numpy as np

    # * Join & Split Functions in NumPy ->
 # join->
# var = np.array([1,2,3,4,5,6,9])
# var2 = np.array([5,6,7,89,4,5])
#
# ar = np.concatenate((var, var2))
# print(ar)
# print()
#
# var3 = np.array([[23,45,64,3],[42,5,6,43]])
# print(var3)
# var4 = np.array([[3,4,6,7],[5,6,7,89]])
# print(var4)
# print()
# ar1 = np.concatenate((var3,var4),axis = 0)
# print(ar1)
# print()
#
# v1 = np.array([2,4,6,7])
# v2 = np.array([2,3,4,6])
# a_new = np.stack((v1,v2),axis = 1)
# print(a_new)
# print()
#
# a_new1 = np.hstack((v1,v2))    #  rows
# print(a_new1)
# print()
#
# a_new2 = np.vstack((v1,v2))   # colums
# print(a_new2)
# print()
#
# a_new3 = np.dstack((v1,v2))   # height
# print(a_new3)
# print()
#
#  # Split->
# var = np.array([3,4,6,7,6,3])
# print(var)
# ar = np.array_split(var,4)
# print(ar)
# print(ar[0])
#
# x = np.array([[4,3,5],[9,8,7],[0,9,7]])
# print(x)
# ar1 = np.array_split(x,4)
# print(ar1)
# print()
#
# ar2 = np.array_split(x,4,axis=1)
# print(ar2)
# print()

    # * Search, Sort,Search Shorted, Filer ->

#Search->

x = np.array([3,5,7,4,3,4,6,3,6,35,6,34])
n = np.where( x == 3 )
print(n)

y = np.array([3,5,7,4,3,4,6,3,6,35,6,34])
n1 = np.where( (x/2) == 3 )
print(n1)

# Search sorted array->
a = np.array([3,4,6,7,8,9,10,11,12,15,17,18,21,22])

x1 = np.searchsorted( a, 5)
print(x1)

a = np.array([3,4,6,7,8,9,10,11,12,15,17,18,21,22])

x2 = np.searchsorted( a, [6,8,9],side = 'right')
print(x2)

# sort Array-:
s = np.array([7,5,6,8,9,3,7,0,6,4,2,5,6,8,6])
print(np.sort(s))

a = np.array(['a','f','f','t','t','e','w','s'])
print(np.sort(a))

w = np.array([[2,3,5,6],[7,6,4,3],[7,4,32,2]])
print(np.sort(w))
print()
  # Filter ->

m  = np.array([3,5,7,2,4,9])
f = [True,False,True,True,False,True]

f_1 = m[f]
print(f_1)