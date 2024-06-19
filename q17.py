#Program in python that converts a given string to title case

'''LOGIC-first we take the string as input.Then we split the string to get the
words.Then we apply loop in the words to capitalize the first letter.'''

string=str(input("enter a string"))
word=string.split()
for i in word:
    i=i.title()
    print(i)
