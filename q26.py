#Program in python that checks if a string starts with a given prefix or ends
#with a given suffix

string=str(input("enter a string"))
pre=str(input("enter a prefix"))
suf=str(input("enter a suffix"))
if string.startswith(pre):
    print("string starts with prefix")
elif string.endswith(suf):
    print("string ends with suffix")
else:
    print("neither")
