    # Q1-> Created nested dictionary-:

details = {
    'name' : 'nikhil bhandari',
    'age' : 22,
    'qualifications' : 'B-Tech',
    'Branch' : 'CSE',
    'Address' : {
        'door no' : 110,
        'street' : 'nagraja mahoola',
        'city' : 'srinagar garhwal',
        'state' : 'uttrakhand',
    }
}
print(details)

    # Q2-> Convert two lists into a dictionary-:

list1 = [1,2,3,4,5,6]
list2 = [1,4,9,16,2,15,36]

my_dict = {}
for index, value in enumerate(list1):

   # -> enumerate() gives you both index and value:
   my_dict[value] = list2[index]

my_dict2 = {k:v for k, v in zip(list1,list2)} # k -> key, v -> value 

my_dict3 = dict(zip(list1, list2))

print(my_dict)
print(my_dict2)
print(my_dict3)




