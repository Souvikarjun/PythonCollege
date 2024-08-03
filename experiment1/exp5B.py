# swapping numerical

str1 =  input("input 1st string: ")
str2 =  input("input 2nd string: ")

# using third variable 

temp = str1
str1 = str2
str2 = temp

print("After swapping with a third variable, numbers are\n",str1,str2)

# without third variable

str1 , str2 = str2, str1

print("After swapping again without third variable, numbers are\n",str1,str2)