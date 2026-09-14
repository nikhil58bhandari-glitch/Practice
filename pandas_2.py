import pandas as pd

  # Handling Missing Value-:
  #   (dropna & fillna)

# csv1 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\sample_data.csv")
# print(csv1)
# print()

# dropna()-:
# print(csv1.dropna())
# print()
#
# print(csv1.dropna(axis = 1))
# print()
#
# print(csv1.dropna(how = 'all'))
# print(csv1.dropna(how= 'any'))
# print()
#
# # subset-:
# print(csv1.dropna(subset = ['Age']))
# print()
#
# # inplace()-:
# print(csv1.dropna(inplace = True))
# print()

# thresh()-:
# print(csv1.dropna(thresh = 2))
# print()

# Fillna-:

# print(csv1.fillna('Pyhton'))
# print()
#
# print(csv1.fillna({'Age': 55, 'City' : 'Uttrakhand' }))
# print()

# print(csv1.fillna(method = 'ffill'))
# print(csv1.ffill())
# print(csv1.bfill())
# print()
# print(csv1.ffill(axis = 1 ))
# print(csv1.bfill(axis = 1))
# print()

# inpace()-:

# csv1.fillna(12, inplace = True)
# print(csv1)

# print(csv1.fillna('python' , limit = 2))
# print()

     # Handling Missing Values -:
     # (Replace & Interpolate)

# Replace -:

csv1 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\sample_data.csv")
print(csv1)
print()

print(csv1.replace(to_replace=1,value= 22))
print(csv1.replace(to_replace='Priya Singh',value= 'python'))
print()

print(csv1.replace([1,2,3,4,5,6,7,8,9,10],22))
print(csv1.replace('[A-Za-z]','python', regex = True))
print()

print(csv1.replace({'Name':'[A-Z]'}, 22, regex= True))
print()

# print(csv1.replace(1, method= 'ffill'))
# print(csv1.replace(1, method = 'bfill'))

# print(csv1.replace(1,method='ffill',limit = 2))

# print(csv1.replace(1,method='ffill',limit= 3, inplace = True))

# Interpolate()-:

csv2 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\sample_data.csv")
print(csv2)
print()

print(csv2.interpolate())
print()

# print(csv1.interpolate(method = 'linear'))
print(csv2.interpolate(method = 'linear', axis = 0))
# print(csv2.interpolate(method = 'linear', axis = 1))
print()

print(csv2.interpolate(limit = 2))
print(csv2.interpolate(limit_direction = 'forward',limit = 2))
print(csv2.interpolate(limit_direction = 'backward',limit = 2))
print(csv2.interpolate(limit_direction = 'both',limit = 2))

print(csv2.interpolate(limit_area = 'inside'))
print(csv2.interpolate(limit_area = 'outside'))
print(csv2.interpolate(limit_direction = 'both',limit = 2, inplace = True))