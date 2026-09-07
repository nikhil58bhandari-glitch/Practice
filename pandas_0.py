import pandas as pd

# Series-:
x = [2,3,4,6,9]
# a = pd.Series(x)
# a = pd.Series(x,index =['a','b','c','d','e'],dtype='float')
a = pd.Series(x,index =['a','b','c','d','e'],dtype='float', name='python')
print(a)
print(type(a))
# print(a[3])
print()

dic = {'name':['python','c','c++','java','sql'], 'por': [12,23,34,45,56], 'rank':[1,4,3,2,5]}
var = pd.Series(dic)
print(var)
print()

s = pd.Series(12, index =[1,2,3,4,5,6])
print(s)
print(type(s))
print()

s = pd.Series(12, index =[1,2,3,4,5,6])
s1 = pd.Series(12,index=[1,2,3,4])
print(s+s1)
