letter = '''
Welcome to our company 
mr <|name|>
you are selected and your onboarding date is
Date: <|date|>
'''
name = input("Enter Your Name:\n")
date = input("Enter Date: \n")
letter = letter.replace("<|name|>",name) 
letter = letter.replace("<|date|>",date) 
print(letter)