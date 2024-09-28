start = 1
end = 365

Months = {"January", "february","March","April","May","June","July","August","September","October","November","December"}
Week = ["mon","tue","wed","thu","fri","sat", "sun"]

January = []
February =[]
March = []
April = []
May = []
June = []
July = []
August = []
September = []
October = []
November = []
December = []

month_source = int(input("enter a month (1-12): "))
temp = 0

for i in range(1, 13):
    if i == 1:
        January.append("mon")

    elif i == 2:
        temp = temp+(31%7)+1
        if temp==8:
            temp = 0

        February.append(Week[temp-1])

    elif i == 3:
        temp = temp+(29%7)+1
        if temp==8:
            temp = 0
        March.append(Week[temp-1])

    elif i == 4:
        temp = temp+(31%7)+1
        if temp>=8:
            temp = 0
        April.append(Week[temp-1])

    elif i == 5:
        temp = temp+(30%7)+1
        if temp>=8:
            temp = 0
        May.append(Week[temp-1])

    elif i == 6:
        temp = temp+(31%7)+1
        if temp>=8:
            temp = 0
        June.append(Week[temp-1])

    elif i == 7:
        temp = temp+(30%7)+1
        if temp>=8:
            temp = 0
        July.append(Week[temp-1])

    elif i == 8:
        temp = temp+(31%7)+1
        if temp>=8:
            temp = 0
        August.append(Week[temp-1])

    elif i == 9:
        temp = temp+(31%7)+1
        if temp>=8:
            temp = 0
        September.append(Week[temp-1])

    elif i == 10:
        temp = temp+(30%7)+1
        if temp>=8:
            temp = 0
        October.append(Week[temp-1])

    elif i == 11:
        temp = temp+(31%7)+1
        if temp>=8:
            temp = 0
        November.append(Week[temp-1])

    elif i == 12:
        temp = temp+(30%7)+1
        if temp>=8:
            temp = 0
        December.append(Week[temp-1])
    

print(December)