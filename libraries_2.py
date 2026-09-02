import numpy as np

     # * Arithmetic Operations in Numpy Arrays ->

   # Addition -:
# var = np.array([1,2,3,4,5])
# varadd = var + 3
# print(varadd)
#
# var1 = np.array([1,2,3,4,5])
# var2 = np.array([6,7,8,9,10])
#
# varadd = var1 + var2
# print(varadd)
#
# var1 = np.array([1,2,3,4,5])
# var2 = np.array([6,7,8,9,10])
#
# varadd = np.add(var1,var2)
# print(varadd)
# print()
#
#   # Substraction ->
# var = np.array([1,2,3,4,5])
# varsub = var - 3
# print(varsub)
#
# var1 = np.array([1,2,3,4,5])
# var2 = np.array([6,7,8,9,10])
#
# varsub = var1 - var2
# print(varsub)
# print()
#
#    # Multiplication->
# var = np.array([1,2,3,4,5])
# varmul = var * 3
# print(varmul)
#
# var1 = np.array([1,2,3,4,5])
# var2 = np.array([6,7,8,9,10])
#
# varmul = var1 * var2
# print(varmul)
# print()
#
#     # Division ->
# var = np.array([1,2,3,4,5])
# vardiv = var / 3
# print(vardiv)
#
# var1 = np.array([1,2,3,4,5])
# var2 = np.array([6,7,8,9,10])
#
# vardiv = var1 / var2
# print(vardiv)
# print()
#
#    # Modulo->
# var = np.array([1,2,3,4,5])
# varmod = var % 3
# print(varmod)
#
# var1 = np.array([1,2,3,4,5])
# var2 = np.array([6,7,8,9,10])
#
# varmod = np.mod(var1,var2)
# print(varmod)
#
#     # 2D Array -:
# var21 = np.array([[1,2,3,4],[5,6,7,8]])
# var22 = np.array([[6,7,8,9],[10,11,12,13]])
#
# varadd = np.add(var21,var22)
# print(varadd)


  # Arithmetic Functions ->
var = np.array([1,2,3,4,5,6])
print('min : ',np.min(var))
print('max : ',np.max(var))
print('arg max : ',np.argmax(var))
print('arg min : ',np.argmin(var))
print(np.sqrt(var))
print(np.sin(var))
print(np.cos(var))
print(np.cumsum(var))

var1 =np.array([[1,2,3,4,5],[4,5,3,2,6]])
print(np.min(var1,axis = 0))











