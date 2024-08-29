#Armstrong Number
num = int(input("Enter a number: "))

Sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   Sum += digit ** 3
   temp //= 10

if num == Sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Perfect Number
Sum = 0
for i in range(1, num):
    if(num % i == 0):
        Sum = Sum + i
if (Sum == num):
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")


#Adam Number
rev = 0
while (num > 0) : 
    rev = rev * 10 + num % 10
    num //= 10

a = num*num  
b = rev*rev 
revb = 0
while (num > 0) : 
    revb = revb * 10 + num % 10
    b //= 10


if (a == revb) : 
    print ("Adam Number") 
else : 
    print ("Not a Adam Number") 


#Palindrome Number

temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")