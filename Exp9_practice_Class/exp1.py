with open("poems.txt", 'r') as p:
    String = p.read()

Word1 = "Twinkle"
Word2 = "Star"


for char in String:
    if(char != "\n" or char != " "):
        string1 += char
        
