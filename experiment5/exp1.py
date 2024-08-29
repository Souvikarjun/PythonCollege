Amount = float(input("Input the amount: "))

if(Amount<=5000):
    Amount = Amount-(Amount*(5/100))
elif(5000<Amount<=15000):
    Amount = Amount-(Amount*(12/100))
elif(15000<Amount<=25000):
    Amount = Amount-(Amount*(20/100))
else:
    Amount = Amount-(Amount*(15/100))

print("The end Amount is: ",Amount)