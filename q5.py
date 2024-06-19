#Program that takes a string input from the user and writes it to a text file

f=open("India.txt","w")
string=str(input("enter a line"))
f.write(string)
print("content written")
