number = int(input("enter a six digit number: "))

position1=6
position2=1
# listOfNum = ()
sum1 = 0
sum2 = 0

if(len(str(number)) == 6): 
    for digits in str(number) :
        sum1 = sum1 + (int(digits)*10 + position1)
        position1 -= 1

if(len(str(number)) == 6): 
    for digits in str(number) :
        sum2 = sum2 + (int(digits)*10 + position2)
        position2 += 1

    # while number :
    #     sumOfNum = sumOfNum + (int(listOfNum[position])*10 + position)
    #     position +=1 

print("Sum 1 =", sum1)
print("Sum 2 =", sum2)

subtraction = sum1 - sum2

print("subtraction of sum1 and sum2 =", subtraction)