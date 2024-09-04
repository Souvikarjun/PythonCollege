list1 = []

number = int(input("Numbers of element: "))

for i in range(0, number):
    element = int(input("Element of the list: "))
    list1.append(element)

list_Even = []
list_Odd = []

for numbers in list1:
    if numbers%2 == 0 :
        list_Even.append(numbers)
    else :
        list_Odd.append(numbers)

print("First List : ", list1)
print("Even List : ", list_Even)
print("Odd List : ", list_Odd)