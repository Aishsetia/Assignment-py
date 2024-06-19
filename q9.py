#Program that checks if a substring is present in a given string

statements=str(input("enter a string"))
subs=str(input("enter substring you want to check"))
if subs in statements:
    print("found substring")
else:
    print("substring not found")
