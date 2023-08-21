# Dictionary is a collection of key-value pairs
# You can also Create Nested Dictionary

dictionary = {

    "name" : "Darshan",
    "age" : 22,
    "pass" : True,
    "marks" : [1,2,5,8,3],
    "subject" : ['english','sports'],
    "anotherdictionary" : 
    {
        "sports" : ["cricket","football"],
        "wickets" : 425,
        "speed" : 134.90,
    }
}

# it will print the value of the given key

print(dictionary["name"])
print(dictionary["age"])
print(dictionary["pass"])
print(dictionary["marks"])

dictionary['marks'] = [97,56,90]

print(dictionary["marks"])

print(dictionary["subject"])
print(dictionary["anotherdictionary"])
print(dictionary["anotherdictionary"]["sports"])
print(dictionary["anotherdictionary"]["wickets"])
print(dictionary["anotherdictionary"]["speed"])


print(dictionary)

# it is unordered
# it is mutable 
# cannot contain duplicate keys 

