import pandas as pd

# Series-:
x = [2,3,4,6,9]
# a = pd.Series(x)
# a = pd.Series(x,index =['a','b','c','d','e'],dtype='float')
# a = pd.Series(x,index =['a','b','c','d','e'],dtype='float', name='python')
# print(a)
# print(type(a))
# # print(a[3])
# print()
#
# dic = {'name':['python','c','c++','java','sql'], 'por': [12,23,34,45,56], 'rank':[1,4,3,2,5]}
# var = pd.Series(dic)
# print(var)
# print()
#
# s = pd.Series(12, index =[1,2,3,4,5,6])
# print(s)
# print(type(s))
# print()
#
# s = pd.Series(12, index =[1,2,3,4,5,6])
# s1 = pd.Series(12,index=[1,2,3,4])
# print(s+s1)

# Dataframes-:
# x = [3,5,6,8,5,3]
# var = pd.DataFrame(x)
# print(var)
# print(type(var))
#
# d = {'a': [2,3,5,6,7,3], 's':[5,4,3,2,5,4]}
# var1 = pd.DataFrame(d)
# # var1 = pd.DataFrame(d,columns=['a','b'])
# # var1 = pd.DataFrame(d,columns=['a','s'],index=['a','s','d','f','l','n'])
# print(var1)
# print(var1['a'][3])
#
#
# list = [[2,3,4,5],[5,6,7,8],[8,7,6,5],[3,4,5,7]]
# var2 = pd.DataFrame(list)
# print(var2)

# sr = {'s' : pd.Series([3,4,6,5]), 'r' : pd.Series([9,7,0,9])}
# var3 = pd.DataFrame(sr)
# print(var3)

   # Arithmetic Operations -:

# var = pd.DataFrame({'A' :[1,2,3,4], 'B' :[5,6,7,8]})
# print(var)
# print()
# # var['C'] = var['A'] + var['B']
# # var['C'] = var['A'] - var['B']
# # var['C'] = var['A'] * var['B']
# var['C'] = var['A'] / var['B']
# print(var)
# print()
#
# var1 = pd.DataFrame({'A' : [3,6,9,12], 'B' : [4,8,12,16]})
# print(var1)
# print()
# var1['Python'] = var1['A'] <= 10
# var1['Python_1'] = var1['B'] <= 15
# print(var1)

    # Delete and Insert Data in Pandas->

# INSERT-:
var = pd.DataFrame({'A' : [4,6,2,7,9], 'B': [4,8,3,2,1]})
print(var)
# var.insert(1,'python', var['A'])
# print(var)
#
# var.insert(1,'python_1', [11,2,22,33,54])
# print(var)

var['pyhton_2'] = var['A'][:3]
print(var)
print()

# Delete->
var1 = pd.DataFrame({'A' : [4,7,2,7],'B' :[6,3,7,1], 'C' : [66,41,32,36]})
print(var1)
print()
var_1 = var1.pop('B')
print(var_1)
print()
print(var1)

del var['A']
print(var1)
