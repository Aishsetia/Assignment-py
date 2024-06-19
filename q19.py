#Program that removes all punctuation from a given string.

string=str(input("enter a string"))
for i in string:
    if i.isalnum() or i.isspace():
        print(i)
       
