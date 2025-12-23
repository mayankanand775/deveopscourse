#list 
my_list=["apple","banana","cherry"]
# #list are used to store mulitple items in a single variable
# print(my_list)
# #list are ordered ,changeable and allow duplicate values.
# #dublicate
# dublicate=["ana","ana","mayank"]
# print(dublicate)
# #list length
# print(len(dublicate))
# #list with strings,integers and boolean values:
# list1=["abc",34,True,40,"male"]
# print(list1)
# print(type(list1))
# #List constructor
# thislist=list(("apple","cherry","cherry"))
# print(thislist)
# print(my_list[0],my_list[1],my_list[2])
# print(my_list[-1])
list_data=["mayank","rajana","pragati","jash","priya","sunaina"]

#membership operator
if "mayank" in list_data:
    print("i love mayank")
    list_data[0]="Tanya"

#you can replace it also:
list_data[1:3]=["gahina","muski"]
print(list_data)    
list_replace=["apple","banana","cherry"]
list_replace[1:3]=["watermelon"]
print(list_replace) 
#insert without distrubing the existing list
list_dt=['a','b','c','d','e']
list_dt.insert(2,"iloveyou")
print(list_dt)

#insert change item value
thislist=["apple","banana","cherry"]
thislist[1]="blackcurrant"
print(thislist)

listthis=["apple","banana","cherry"]
print(listthis[1:2])
listthis[1:2]=["a","b","c"]
print(listthis)

#remove function remove the first occurrance
print(listthis.remove("a"))
print(listthis)
rt=listthis.pop(2)
print(rt)
#delete the list
del listthis[0]
print(listthis)
#clear list
listthis.clear()
print(listthis)

#list looping
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)