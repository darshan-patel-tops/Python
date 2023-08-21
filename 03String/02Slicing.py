greeting = "Good Morning, "
name = "darshan"

# print(type(name))

# print(greeting + name) #also valid
# c = greeting + name     #Concatination
# print(c)

name1 = input("enter your name: \n")
print("Good Evening,"+name1) #both will work
# print("Good Evening,",name1) #both will work

print(name[0])

print(name[0:4]) #it will print from 0  to 3 (4 will be excluded) same goes for the list
# the first is included and last one is excluded[0:4] 0 will be included and 4 will be excluded
# it is called slicing when you just wanna print a specific part of the string 

# print(name[:4]) is same as [0:4]
# print(name[0:]) #is same as [0:7] because in darshan there are only 6 index inshort it will print till last
# print(name[-4:-1]) #this is called minus indexing it is same as [1:4]

# print(name[0:7:3]) #it will skip the value