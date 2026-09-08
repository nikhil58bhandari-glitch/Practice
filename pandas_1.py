import pandas as pd

    # Write CSV file in Python Pandas -:
      #  (Comma Separated Values)

dis = {'A' : [2,4,5,6,7,5], 'S' : [5,3,6,2,7,9],'D' : [1,9,8,2,3,8]}

d = pd.DataFrame(dis)
print(d)

# d.to_csv('test_new.csv')
# d.to_csv('test_new1.csv', index = False)
d.to_csv('test_new2.csv', index = False,header = [1,2,3] )