import copy

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = list1
# list3 = copy.copy(list1)
# print(list1)
# print(list2)

# list1[1] = 23
# print(list1,list2)

# print(id(list1))
# print(id(list2))
# print(id(list3))
# print(list3)

list1 = [10,20,[30,40]]
list2 = copy.deeps.copy(list1)
list1[2][0] = 40

print(list1, list2)

l1 = ["name1","name2","name3","name4"]

for name in l1 :
    print(name)