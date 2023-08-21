
dictionary = {

    "name" : "Darshan",
    "age" : 22,
    "pass" : True,
    1 : 2,
    "marks" : [1,2,5,8,3],
    "subject" : ['english','sports'],
    "anotherdictionary" : 
    {
        "sports" : ["cricket","football"],
        "wickets" : 425,
        "speed" : 134.90,
    }
}

print(type(dictionary))

print(list(dictionary))

# Dictionary Methods

# Prints the keys of the dictionary
print(dictionary.keys())

# Prints the values of the dictionary
print(dictionary.values())

# Prints the (key,value) for all contents of the dictionary
# Prints in the format of Tuple
print(dictionary.items())

upatedictionary = {
    "city" : "Ahmedabad"
}

# Updates the dictionary by adding key-value pairs from upatedictionary
dictionary.update(upatedictionary)

print(dictionary)

# The difference between .get and [] syntax in Dictionaries
print(dictionary.get("name")) # Return value associted with key name
print(dictionary["name"]) # Return value associted with key name

print(dictionary.get("name1")) # It will try to get if it exists otherwise will give none
print(dictionary["name1"])  # It will try to look for it and if it does exists then it will throw an error