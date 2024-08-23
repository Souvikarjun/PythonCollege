import math

"""#functions of strings
mili_shayari = '''Hey Mili you are my butterfly
                    without Mili i will die
                    but Mili always makes me cry'''

jhilli_shayari= mili_shayari.replace("Mili","Jhilli")
print(jhilli_shayari)

print(mili_shayari.lower())     #convert enture string to lowercase
print(mili_shayari.upper())     #convert entire string to uppercase
print(mili_shayari.swapcase())  #covert capital letters to small and vice-versa

temp="we know what we are"
print(temp.capitalize())    #capitalize first letter of first word
print(temp.title())         #capitalize first letter of all words

print(temp.index("k"))      #index function- retuens the index value
print(temp.index("w",1))     #index("value",start,end) therefore gives the index value of w starting from 1
print(temp.index("w",temp.index("w")+1))     #when we dont have prior info about the string
print(temp.index("w",temp.index("w",temp.index("w")+1)+1))

print(temp.rindex("w"))     #returns index from last
# print(temp.rindex("w",1))
# print(temp.rindex())

print(temp.count("we"))     #counts the no. of occurance of substring in the string
print(temp.split())         #splits the string according to the blank space
print(temp.split("w"))      #splits the string considering w

print(temp.find("q"))       #returns -1 for the char not present
# print(temp.index("q"))      #gives error

#list
crush_list = ["milli","jhilli","sonali","rupali"]
(crush_list.append("silli"))            #adds string inn the list
print(crush_list)
(crush_list.insert(2,"monali"))    #inserts the string after the given index in list, index("index","value")
print(crush_list)

print(crush_list.pop())         #removes lasat index value from string permanently
print(crush_list)

crush_list.remove("jhilli")
print(crush_list)

crush_list.clear()
print(crush_list)

crush_list = ["milli","jhilli","sonali","rupali","jhilli"]
print(crush_list.count("jhilli"))
print(crush_list.index("milli"))

new= crush_list.copy()
print(new)

list1=[2,6,7,4,9,3,0,56]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

list2=[1,4,"milli","c"]     #can store heterogenous bvalues but cant be operated
print(list2)

list3=["milli","jhilli","sonali","rupali","jhilli"]
list3.sort()                #arranges the strings in alphabetical order
print(list3)

#dictionary
crush_info={"milli":20,"jhilli":18, "rupali":19, "sonali":22}
crush_info.clear()
print(crush_info)
crush_info={"milli":20,"jhilli":18, "rupali":19, "sonali":22}
new = crush_info.copy()
print(new)
print(new["rupali"])
print(new.get("rupali"))        #two methods because if we fetch a value not present in our dict then it will retuen -1 whereas in prev case it will show error

print(new.items())             #returns each value in the form of list 

print(new.keys())               #returns only the keys
print(new.values())             #returns only the values

new.pop("rupali")               #removing an element from dict
print(new)

new["rupali"]=23                #adding a new elemet in dict
print(new)

new.popitem()                   #removing the last item
print(new)

#tupple
tup1=(1,2,5,6,33,2,5)
print(tup1.count(2))
print(tup1.index(5))

p = eval(input("input: "))

print(p) """

Let=(1,2,5,6,33,2,5)
print(min(Let))
print(max(Let))

new = math.ceil(29.8)
print(new)
print(math.fabs(-9))