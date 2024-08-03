# Calculate time for simple interest

principal = float(input("Input principle amount:"))
interest = float(input("Input interest:"))
rate = float(input("Input rate of interest:"))

rate = rate/100

time = round(interest/(principal*rate),2)

print("the time is: ",time,"years")