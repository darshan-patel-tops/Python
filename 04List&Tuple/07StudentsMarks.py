# Writing int around input field will make the input in int data type because by default 
# it is string

m1 = int(input("Enter marks for student 1 : \n"))
m2 = int(input("Enter marks for student 2 : \n"))
m3 = int(input("Enter marks for student 3 : \n"))
m4 = int(input("Enter marks for student 4 : \n"))
m5 = int(input("Enter marks for student 5 : \n"))
m6 = int(input("Enter marks for student 6 : \n"))


studentsmarks = [m1,m2,m3,m4,m5,m6]

print("My student list is",studentsmarks)

studentsmarks.sort()
print(studentsmarks)



a = [1,56,2,4]

print(sum(a))
print(a[0]+a[1]+a[2]+a[3])
# Both are correct 