with open("text.txt","r") as a:
    Text =  a.readlines()
ch=0
w=0
li=0

for lines in Text:
    for char in lines:    
        if(char != " " or char != "\n"):
            ch += 1
        if(char == " " or char == "\n"):
            w += 1
    li += 1

print(ch, w, li)
