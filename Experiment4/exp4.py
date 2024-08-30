last_number = 100
Sum = 0

for number in range(11, last_number + 1):

    i = 2
    for i in range(11, number):
        if (int(number % i) == 0):
            i = number
            break

    if i is not number:
        Sum = Sum + number
print("\nThe sum of prime numbers in python from 1 to 100 is:", Sum)
