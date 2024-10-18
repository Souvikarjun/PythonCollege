Frequent = {}

with open('text.txt', 'r') as a:
    String = a.read()

for char in String:
    if(char not in Frequent):
        new = [(char,1)]
        Frequent.update(new)
    else:
        Frequent[char] += 1


print(Frequent)