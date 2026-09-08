import pandas as pd

    # Write and Read CSV file in Python Pandas -:
      #  (Comma Separated Values)

# dis = {'A' : [2,4,5,6,7,5], 'S' : [5,3,6,2,7,9],'D' : [1,9,8,2,3,8]}
#
# d = pd.DataFrame(dis)
# print(d)
#
# # d.to_csv('test_new.csv')
# # d.to_csv('test_new1.csv', index = False)
# d.to_csv('test_new2.csv', index = False,header = [1,2,3] )

# read -:

csv1 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv")
print(csv1)
print()

# csv2 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", nrows = 4)
# print(csv2)
# print(type(csv2))
# print()
#
# csv3 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", usecols = [0,3]) #['Student_ID', 'Name'])
# print(csv3)
# print(type(csv3))
# print()

# csv4 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", skiprows = [0,3])
# print(csv4)
# print(type(csv4))
# print()

# csv5 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", index_col = 'Name')
# print(csv5)
# print(type(csv5))
# print()
#
# csv6 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", header = 2)
# print(csv6)
# print(type(csv6))
# print()

# csv7 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", names = ['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10'])
# print(csv7)
# print(type(csv7))
# print()
#
# csv8 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", header = None, prefix='col')
# print(csv8)
# print()

csv9 = pd.read_csv("C:\\Users\\nikhi\\Downloads\\students_pandas_practice.csv", dtype ={'Age' : 'float'})
print(csv9)
print()


