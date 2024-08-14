string1 = str(input("Input first string: "))
string2 = str(input("Input first string: "))
i = 0
string3 =""
for substring in string1:
    string3 = string3 + string1[i]+string2[i]
    i +=1

print(string3)