def Addition(x,y):
    Addition = x+y
    return Addition

def Subtraction(x,y):
    Subtraction = x-y
    return Subtraction

def Multiplication(x,y):
    Multiplication = x*y
    return Multiplication

def Division(x,y):
    Division = x/y
    return Division


def main():
    X = float(input("input X: "))
    Y = float(input("input Y: "))

    print("Addition = ", Addition(X,Y))
    print("Subtraction = ", Subtraction(X,Y))
    print("Multiplication = ", Multiplication(X,Y))
    print("Division = ", Division(X,Y))


if __name__ == '__main__':
    main()