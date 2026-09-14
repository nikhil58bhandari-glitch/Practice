import pandas as pd

    # merging & concat -:

# merge()-:

var1 = pd.DataFrame({'A':[2,4,6,8,10,12], 'B':[1,3,5,7,9,11]})
print(var1)
print()

var2 = pd.DataFrame({'A' :[2,4,6,8,10,22],'C':[11,13,15,17,19,21]})
print(var2)

print(pd.merge(var1,var2,on = 'A'))
print()
print(pd.merge(var2,var1,on = 'A'))

print(pd.merge(var1,var2,how = 'inner'))
print(pd.merge(var1,var2,how = 'left'))
print(pd.merge(var1,var2,how = 'right'))
print(pd.merge(var1,var2,how = 'outer'))
print()

print(pd.merge(var1,var2,how = 'outer',indicator = True))

print(pd.merge(var1,var2, left_index = True, right_index = True ))

print(pd.merge(var1,var2, left_index = True, right_index = True, suffixes = ('name', 'value')))
print()
# concat()-:

sr1 = pd.Series([2,3,4,5,6,7])
sr2 = pd.Series([11,21,31,41,51,61])
print(sr1,sr2)

print(pd.concat([sr1,sr2]))

d1 = pd.DataFrame({'A':[2,4,6,8,10,12], 'B':[1,3,5,7,9,11]})
print(d1)
print()

d2 = pd.DataFrame({'A' :[2,4,6,8,10,11],'B':[11,13,15,17,19,21]})
print(d2)
print(pd.concat([d1,d2]))
print()

print(pd.concat([d1,d2], axis = 1))
print()

print(pd.concat([d1,d2], axis = 1,join = 'inner'))
print(pd.concat([d1,d2], axis = 1,keys = ['d1', 'd2']))

