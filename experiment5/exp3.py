Numbers = [10, 20, 22, 0, -40, -35, 0, 100, -20]

positive_count = 0
negative_count = 0
zero_count = 0

for number in Numbers:
    if number<0:
        negative_count += 1
    elif number>0:
        positive_count += 1
    else:
        zero_count += 1


print("List of numbers: ", Numbers)

print("positive count: ", positive_count)
print("negative count: ", negative_count)
print("zero count: ", zero_count)