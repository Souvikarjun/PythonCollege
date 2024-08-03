# swapping numerical

Num1 =  input("input 1st number")
Num2 =  input("input 2nd number")

# using third variable 

temp = Num1
Num1 = Num2
Num2 = temp

print("After swapping with a third variable, numbers are\n",Num1,Num2)

# without third variable

Num1 , Num2 = Num2, Num1

print("After swapping again without third variable, numbers are\n",Num1,Num2)