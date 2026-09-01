import numpy as np

      # * Arrays with Random Numbers->

    # "rand()" ->
# var = np.random.rand(4)
# print(var)
# print()
#
# var1 = np.random.rand(2,5)
# print(var1)
# print()

    # "randn()" ->
# var2 = np.random.randn(5)
# print(var2)
# print()

# var3 = np.random.randn(3,5)
# print(var3)
# print()

    # "ranf()" ->
# var4 = np.random.ranf(5)
# print(var4)
# print()

# var5 = np.random.ranf((3,4))
# print(var5)
# print()

    # "randint()" ->
# var6 = np.random.randint(5,20 , 5)
# print(var6)
# print()

# var7 = np.random.randint(5,50,(3,4))
# print(var7)


     # * What is Data Type of Numpy Array / DataType function ->

var = np.array([1,2,3,4,34,65,86,34])
print("Data Type : ", var.dtype)

var1 = np.array([1.0,2.3,3.4,4.5,34.3,65.1,86.8,3.4])
print("Data Type : ", var1.dtype)

var2 = np.array(['N','I','K','H','I','L'])
print("Data Type : ", var2.dtype)

var3 = np.array(['N','I','K','H','I','L',1,2,3,4,5])
print("Data Type : ", var3.dtype)


x = np.array([1,2,3,4,5], dtype = np.int8)
print("Data Type : ", x.dtype)
print(x)

x1 = np.array([1,2,3,4,5], dtype = 'f')
print("Data Type : ", x1.dtype)
print(x1)

x2 = np.array([1,2,3,4,5])
new = np.float32(x2)
new1 = np.int_(x2)
print("Data Type : ", x2.dtype)
print("DataType: ", new.dtype)
print("Data Type: ", new1.dtype)
print(x2)
print(new)
print(new1)

x3 = np.array([1,2,3,4,5])
new2 = x3.astype(float)
print(x3)
print(new2)
