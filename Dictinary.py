    # Q1-> Created nested dictionary-:

# details = {
#     'name' : 'nikhil bhandari',
#     'age' : 22,
#     'qualifications' : 'B-Tech',
#     'Branch' : 'CSE',
#     'Address' : {
#         'door no' : 110,
#         'street' : 'nagraja mahoola',
#         'city' : 'srinagar garhwal',
#         'state' : 'uttrakhand',
#     }
# }
# print(details)

    # Q2-> Convert two lists into a dictionary-:

# list1 = [1,2,3,4,5,6]
# list2 = [1,4,9,16,2,15,36]
#
# my_dict = {}
# for index, value in enumerate(list1):
#
#    # -> enumerate() gives you both index and value:
#    my_dict[value] = list2[index]
#
# my_dict2 = {k:v for k, v in zip(list1,list2)} # k -> key, v -> value
#
# my_dict3 = dict(zip(list1, list2))
#
# print(my_dict)
# print(my_dict2)
# print(my_dict3)

   # Q3-> Iterate over Dictionaries using for loop -:

# my_dict = {'A' : 'APPEND', 'B':'BASECLASS', 'C':'CASE SENDER', 'D':'DATE BASE', 'E':'EFFICIENT'}
#
# for item,value in my_dict.items():   # .items() → gives key + value
#     print(f"{item} for {value}")
#
# for item in  my_dict.keys():       # .keys() → gives only keys
#     print(item, end=' ')
# print()
#
# for value in my_dict.values():   #  .values() → gives only values
#     print(value, end=' ')
#
# print()


    # Q4-> Sort  a dictionaty by value -:

# my_dict = {2:'pineapple', 3 : 'banana', 4: 'orange', 11 :'papaya'}
#
# # sorted_dict = dict(sorted(my_dict.items(), key = lambda x:x[1]))
# sorted_dict = dict(
#     sorted(              # sorted() needs to know what it should sort by
#         my_dict.items(),
#         key=lambda x: x[1]    #  lambda x: x[1]-> Take one item and return its value.
#     )                                      #  What does key= mean?-> "When sorting, use the second element of each item."
# )
# print(sorted_dict)
#
# # print(dict(sorted(my_dict.items(), key = lambda x : x [1], reverse = True)))
# print(
#     dict(
#         sorted(
#             my_dict.items(),
#             key=lambda x: x[1],
#             reverse=True   # Sort in the opposite direction.
#         )
#     )
# )
# will_sorted = list(my_dict.items())
# will_sorted.sort(key = lambda x : x[1])
# print({key:value for key, value in will_sorted})


    # Q5-> Check if a key is present in a dictionary ->

my_dict = {'A' : 'APPEND', 'B':'BASECLASS', 'C':'CASE SENDER', 'D':'DATE BASE', 'E':'EFFICIENT'}

ele = 'N'

if  ele in my_dict.keys():
    print(f'{ele} key exist with {my_dict[ele]}')
else:
    print(f'{ele} not found')

ele = 'C'
if my_dict.get(ele) is not None:
    print(f"{ele} key is present in dictionary with {my_dict.get(ele)}")
else:
    print(f'{ele} key is not in dictionary')


  # Q6-> Delete an item form a dictinaries ->

my_dict = {'A' : 'APPEND', 'B':'BASECLASS', 'C':'CASE SENDER', 'D':'DATE BASE', 'E':'EFFICIENT'}
del my_dict['B']
my_dict.pop('E')
print(my_dict)


   # Q7-> Marge Two Dictionaries ->

one = {1:'Luffy', 2 : 'Zoro', 3: 'Nami', 4: 'Usoop', 5: 'Sanji'}
two = {6:'Choper', 7:'Robin', 8:'Franky', 9 :'Brook', 10: 'Jinbe' }

one.update(two)
print(one)

merged = {**one, **two}
print(merged)