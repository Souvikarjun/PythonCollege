# Calculate rate of interest for simple interest

principal = float(input("Input principle amount:"))
interest = float(input("Input interest:"))
time = float(input("Input time:"))

rate = round(interest/(principal*time),2)
rate = rate*100

print("the rate of interest is: ",rate,"%")