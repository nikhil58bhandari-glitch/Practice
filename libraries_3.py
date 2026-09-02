import numpy as np

   #  * Iterating NumPy Arrays -:
x = np.array([9,8,7,6,5,4,3])
print(x)
for i in x:
    print(i)

y = np.array([[9,8,7,6],[6,5,4,3]])
print(y)
for j in y:
    print(j)
for k in y:
    for l in k:
        print(l)

z = np.array([[[9,8,7],[7,6,5],[5,4,3]]])
print(z)
for i in z:
    for k in i:
        for j in k:
            print(j)

 # nditer() -:
# z1 = np.array([[[9,8,7],[6,5,4],[3,2,1]]])
# for i in np.nditer(z1):
#     print(i)

z1 = np.array([[[9,8,7],[6,5,4],[3,2,1]]])
for i in np.nditer(z1,flags =['buffered'],op_dtypes=['S']):
    print(i)


    # ndenumerate()
z1 = np.array([[[9,8,7],[6,5,4],[3,2,1]]])
for i in np.ndenumerate(z1):
    print(i)

