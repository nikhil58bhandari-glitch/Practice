      # Q1-> Check if list is empty -:

# list1 = [21,3,42,44,65,2,1,22]
# list2 = []
#
# if len(list1) == 0:
#     print("list1 is empty")
# else:
#     print(f"list1 has {len(list1)} elements")
#
# if not list2:
#     print("list2 is empty")


       # Q2-> Get the Last Element of the list -:

# list1 = [43,4,3,6,8,7,6]
# print(list1[len(list1) - 1])
# print(list1 [- 1])


      # Q3-> Index of list using For Loop -:

# list1 = [1,2,3,4,5,6,7,8]
# for i in list1:
#     index = list1.index(i)
#     print(index, "index is-:",i)


     # Q4-> Count the occurance of the item in list -:

# list1 = [2,3,3,3,2,2,3,4,35,2,2,45,6]
# print(list1.count(3))    # count method

     # Q5-> Slice list -:

# print(list1[:3])  # Get first three item
# print(list1[-3:]) # get the last three item
# print(list1[ 1::2])  # get every item starting from the second item
# print(list1[::-1])   # get the reverse list

    # Q6-> Concatenate Two list -:

# list2 = [10,20,30,40,5-0,60,70,80,90]
# print(list1 + list2)
# list1.extend(list2)
# print(list1)
#
# str1 = ['n','i','k','h','i','l']
# str2 = ['b','h','a','n','d','a','r','i']
# print('_'.join(str1 +str2))

     # Q7-> Split a list into evenly sized chunks-:

# size = 2
# lists = [list1[i : i + size] for i in range(0, len(list1), size)]
# print(lists)

    # Q8-> Flattened list from nested list-:

nested_list = [0.1,0.2,[3.1,4.2,[5,6,[70,80,[900,1000]]]]]
def flattened(num):
    flattened_list = []
    for i in num:
        if isinstance(i , list):
            flattened_list.extend (flattened(i))
        else:
            flattened_list.append(i)
    return flattened_list
print(flattened(nested_list))

    # Q9-> Iterate through two lists in parallel-:

list1 = [1,2,3,4]
list2 = list1[::-1]

for  i ,j in zip(list1,list2):
    print(i,j)


    # Q10-> Remove Duplicates :

my_list =[1,2,3,4,5,6,7,7,6,5,4,3,2,1]
print(list(set(my_list)))

new_list = []
for i in my_list:
    if i  not in new_list:
        new_list.append(i)
new_list.sort()   # it sort the list
print(new_list)

new_list = [1,2,3,4,5,6,7,8]
print(f"actual list {new_list}")
del new_list[3]  # delete the 3rd index item
print(f"delete list {new_list}")
new_list.remove(6)  # remove element which we passed as an argument
print(f"remove the item {new_list}")
new_list.pop(2)   # pop item in 2nd index
print(f"pop item {new_list}")