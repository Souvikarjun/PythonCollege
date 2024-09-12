def Addition(T):
    Sum = 0
    for numbers in T:
        Sum =  Sum + numbers

    return Sum

def Multiplication(T):
    Product = 1
    for numbers in T:
        Product =  Product * numbers

    return Product

def inputFuc():
    N = int(input("input the number of element in the tuple: "))
    tuple1 = ()
    for i in range(0,N):
        element = float(input("Input elements: "))
        tuple1 = tuple1 + (element,)
    return tuple1

def main():
    tuple1 = inputFuc()
    Sum = Addition(tuple1)
    Product = Multiplication(tuple1)

    print("Addition = ", Sum)
    print("Multiplication = ", Product)

if __name__ == '__main__':
    main()