# story = '''once upon a time there was a man who lived and 
# had many great memories'''

story = "once upon a time there was a man who lived and had many great memories"

# print(story[0:5])

#String Functions

print(len(story)) #will return length
print(story.endswith("memories")) #will return true or false
print(story.count("a")) #print(story.count("memories")) it will check both
print(story.capitalize()) #in blank it will make the first word capital it receives no arguement
print(story.find("man")) #will find the index of that word in string it will only give it's first occurance even there is a same word in upcoming string
print(story.replace("man","boy"))# will replace the word with the new one
