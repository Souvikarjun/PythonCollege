#for practice purpose only

# def square():
#     for i in range(0,7):
#         print("*******")

def area(hight, width=2):
    area = hight*width
    return area

def main():
    hight = float(input("inout hight: "))
    width = float(input("inout width: "))
    Area = area(hight, width)
    print(Area)

if __name__=='__main__':
    main()
