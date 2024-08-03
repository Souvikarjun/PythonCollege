# Simple and Cumulative interest

principal = float(input("Input principle amount:"))
rate = float(input("Input rate of interest in percentage:"))
time = float(input("Input time:"))

rate = rate/100

simpleInterest = round(principal*rate*time,2)
cumulativeInterest = round(principal*(1+rate)**time -principal,2)

print("the simple interest is: ",simpleInterest)
print("the cumulative interest is: ",cumulativeInterest)