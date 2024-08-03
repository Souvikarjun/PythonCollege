pi = 3.1416

# Calculating area of triangle

triangleHeight = float(input("Input Hight: "))
triangleBase = float(input("Input Base: "))

triangleArea = 0.5*triangleHeight*triangleBase

print("The area of triangle is: ", triangleArea)

# Calculating area of rectangle

rectangleLength = float(input("Input Length: "))
rectangleWidth = float(input("Input width: "))

rectangleArea = rectangleLength*rectangleWidth

print("The area of Rectangle is: ", rectangleArea)

# Calculating area of circle

circleRadius = float(input("Input Circle Radius: "))

circleArea = pi*(circleRadius**2)

print("The area of circle is: ", circleArea)

# Calculating area of sphere

sphereRadius = float(input("Input Sphere Radius: "))

sphereArea = 4*pi*(sphereRadius**2)

print("The area of sphere is: ", sphereArea)