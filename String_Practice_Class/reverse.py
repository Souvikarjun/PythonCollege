with open("text.txt", "r") as a:
    String = a.readlines()

print(String[::-1])