import Addition

def main():
    X = float(input("Input first Number: "))
    Y = float(input("Input Second Number: "))

    Sum = Addition.Addition(X, Y)

    print("Sum of X and Y = ",Sum)

if __name__=='__main__':
    main()