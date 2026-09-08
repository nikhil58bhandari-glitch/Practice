import pandas as pd

  # Handling Missing Value-:
  #   (dropna & fillna)

csv1 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\sample_data.csv")
print(csv1)
print()

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

print(csv1.fillna('Pyhton'))
print()

print(csv1.fillna({'Age': 55, 'City' : 'Uttrakhand' }))
print()

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

print(csv1.fillna('python' , limit = 2))
print()

