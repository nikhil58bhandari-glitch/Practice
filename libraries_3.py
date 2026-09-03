import numpy as np

   #  * Iterating NumPy Arrays -:
# x = np.array([9,8,7,6,5,4,3])
# print(x)
# for i in x:
#     print(i)
#
# y = np.array([[9,8,7,6],[6,5,4,3]])
# print(y)
# for j in y:
#     print(j)
# for k in y:
#     for l in k:
#         print(l)
#
# z = np.array([[[9,8,7],[7,6,5],[5,4,3]]])
# print(z)
# for i in z:
#     for k in i:
#         for j in k:
#             print(j)
#
#  # nditer() -:
# # z1 = np.array([[[9,8,7],[6,5,4],[3,2,1]]])
# # for i in np.nditer(z1):
# #     print(i)
#
# z1 = np.array([[[9,8,7],[6,5,4],[3,2,1]]])
# for i in np.nditer(z1,flags =['buffered'],op_dtypes=['S']):
#     print(i)
#
#
#     # ndenumerate()
# z1 = np.array([[[9,8,7],[6,5,4],[3,2,1]]])
# for i in np.ndenumerate(z1):
#     print(i)


    # Shape & Reshaping in NumPy Array ->

# var = np.array([[1,2,7,6],[3,5,3,4],[76,45,53,3]])
# print(var)
# print(var.shape)
#
# var1 = np.array([2,23,4,5],ndmin = 5)
# print(var1)
# print(var1.shape)
#
# # Reshape ->
# var2 = np.array([4,5,7,5,4,9,2,3,4,5])
# print(var2)
# print(var2.ndim)
# x  = var2.reshape(5,2)
# print(x)
# print(x.ndim)
#
# var3 = np.array([4,5,7,5,4,9,2,3,4,5,11,12])
# print(var3)
# print(var3.ndim)
# print()
#
# x1  = var3.reshape(2,3,2)
# print(x1)
# print(x1.ndim)
#
# print()
#
# one = x1.reshape(-1)
# print(one)
# print(one.ndim)

      # * Broadcasting in NumPy Array -:

# var1 = np.array([1,2,3])
# print(var1)
# print(var1.shape)
# print()
# var2 = np.array([[1],[2],[3]])
# print(var2)
# print(var2.shape)
# print()
# # print(var1 + var2)
#
# var3 = np.array([[2],[5]])
# print(var2)
# print(var3.shape)
#
# var4 = np.array([[4,5,7],[7,64,3]])
# print(var4)
# print(var4.shape)
# print(var3 + var4)

    # Copy And Shape ->

var = np.array([3,5,42,5])
co = var.copy()

# var[1] = 40
print('var : ', var)
print('copy : ', co)

print()

x = np.array([7,6,4,64])
vi = x.view()
x[1] = 99
print('x : ', x)
print('vi : ', vi)