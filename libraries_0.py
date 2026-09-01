import numpy as np

# print(np.__version__)
# y = [1,2,3,4,5]
# print(y)
# print(type(y))


   # Array->

a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))

x = [1,2,3,4,5]
y = np.array(x)
# print(y)
# #
# # l = []
# # for i in range(1,5):
# #     int_1 = int(input('enter-: '))
# #     l.append(int_1)
# # print(l)
#
#
#    # ** Types of Array->
#
#  # ONE Dimensional -:
# y = np.array([1,2,3,4,5,6,5])
# print(y)
# print(y.ndim)  # .ndim tell the dimensional of array

  # TWO Dimensional -:
# arr2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr2)
# print(arr2.ndim)

  # THREE Dimensional -:
# arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr3)
# print(arr3.ndim)


  # N- Dimensional -:
# arrn = np.array([1,2,3],ndmin = 10)
# print(arrn)
# print(arrn.ndim)


       # Array using Numpy functions->

   # Array filled with 0's->   ".zeros"
arr_0 = np.zeros(4)
print(arr_0)
print()

arr_1 = np.zeros((3,4))
print(arr_1)
print()

   # Array filled with 1's->   ".ones"
arr1 = np.ones(4)
print(arr1)
print()

arr2 = np.ones((3,4))
print(arr2)
print()

   # Create an array ->  ".empty"
arr_empty = np.empty(4)
print(arr_empty)
print()

   # An array with a range of element->  ".arange"
arr_range = np.arange(4)
print(arr_range)
print()

   # Array diagonal element filed with 1's->  ".eye"
arr_diagonal = np.eye(3)
print(arr_diagonal)
print()

arr_dia = np.eye(3,5)
print(arr_dia)
print()

   # Create an array with value that  are spaced
   # linearly in specified interval ->  ".linespace"
arr_lin = np.linspace(0,20,num = 5)
print(arr_lin)

