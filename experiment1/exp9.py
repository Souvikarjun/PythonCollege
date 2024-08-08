# calculating a equation

x = float(input("the value of x: "))
y = float(input("the value of y: "))
n = float(input("the value of n: "))

if (n>=2 and n<=8) :
    result = ((((x**2)+(x**3))/((y/4)+(y/3)+(y**8)))**(2*n))*(((y**6)+(y**2))/(x**9))
    print(result)
else :
    print("invalid value of n")