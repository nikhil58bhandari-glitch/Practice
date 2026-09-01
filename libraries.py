import numpy as np

print(np.__version__)
y = [1,2,3,4,5]
print(y)
print(type(y))


   # Array->

a = np.array([1,2,3,4,5])
print(a)
print(type(a))

x = [1,2,3,4,5]
y = np.array(x)
print(y)
#
# l = []
# for i in range(1,5):
#     int_1 = int(input('enter-: '))
#     l.append(int_1)
# print(l)


   # ** Types of Array->

 # ONE Dimensional -:
y = np.array([1,2,3,4,5,6,5])
print(y)
print(y.ndim)  # .ndim tell the dimensional of array

  # TWO Dimensional -:
arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)
print(arr2.ndim)

  # THREE Dimensional -:
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr3)
print(arr3.ndim)


  # N- Dimensional -:
arrn = np.array([1,2,3],ndmin = 10)
print(arrn)
print(arrn.ndim)



