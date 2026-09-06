import numpy as np

  # Insert and Delete ->

# Insert
# p = np.array([2,3,4,5,6])
# print(p)
# v = np.insert(p,4,9)
# v = np.insert(p,(3,1,4),9)
# print(v)
# print()
#
# p1 = np.array([[2,3,4,5,6],[9,8,7,6,5],[9,8,7,5,3]])
# print(p1)
# print()
# v1 = np.insert(p1, 2, 6, axis = 0)
# print(v1)
#
# # Delete->
# p = np.array([2,3,4,5,6])
# print(p)
# v = np.delete(p,2)
# print(v)


   # Concept of Matrix in NumPy python->

var = np.matrix([[1,2],[4,5]])
var2 = np.matrix([[1,2],[4,5]])
print(var)
print(type(var))
print(var + var2)
print()
print(var * var2)
print()
print(var.dot(var2))
print()

var1 = np.array([[1,2,3],[4,5,6]])
print(var1)
print(type(var1))
print(var1 * var1)
print()

# transpose-:
x = np.array([[2,3,4,5],[5,4,7,8]])
print(x)
print(np.transpose(x))
print()
print(x.T)
print()

# swapaxes-:
print(np.swapaxes(x,0,1))
print()
y = np.array([[2,4],[9,8]])
print(y)
print(np.swapaxes(y,0,1))
print()

# inverse-:
z = np.matrix([[3,5],[7,6]])
print(z)
print(np.linalg.inv(z))
print()

# power-:
z1 = np.matrix([[3,5],[7,6]])
print(z1)
print(np.linalg.matrix_power(z1,2))
print()
print(np.linalg.matrix_power(z1,0))
print()
print(np.linalg.matrix_power(z1,-2))

# determinate-:
z2 = np.matrix([[3,5],[7,6]])
print(np.linalg.det(z2))
