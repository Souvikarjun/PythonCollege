list1 = []
list2 = []

common_list = []

n = int(input("Input First list size: "))
m = int(input("Input Second list size: "))

print("Input first list: ")
for i in range(0,n):
    element = int(input("input elements: "))
    list1.append(element)

print("Input second list: ")
for i in range(0,m):
    element = int(input("input elements: "))
    list2.append(element)

for number1 in list1:
    for number2 in list2:
        if number1 == number2:
            common_list.append(number1)

print("Common List: ", common_list)