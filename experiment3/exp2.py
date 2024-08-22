Element_X = float(input("Input first Number: "))
Operation = str(input("Chose operation from +,-,*,/,%,<<,>> : "))
Element_Y = float(input("Input Second Number: "))
Output = 0

if(Operation == "+"):
    Output = Element_X+Element_Y
if(Operation == "-"):
    Output = Element_X-Element_Y
if(Operation == "*"):
    Output = Element_X*Element_Y
if(Operation == "/"):
    Output = Element_X/Element_Y
if(Operation == "%"):
    Output = Element_X%Element_Y
if(Operation == "<<"):
    Output = int(Element_X)<<int(Element_Y)
if(Operation == ">>"):
    Output = int(Element_X)>>int(Element_Y)

print("Output = ",Output)