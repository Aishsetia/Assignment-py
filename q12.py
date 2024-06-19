#Program that calculates the sum of the digits of a given number

'''LOGIC-First taking an input from the user as integer,convert to string so
that we can store digits as individual elements of list.Then run a loop with
range upto length of list(number of digits in the number).Now a stores the
remainder of the number i.e the last digit and keeps adding.The number is
being updated each time by integer division.'''

num=int(input("enter a number"))
string=str(num)
l=list(string)
length=len(l)
sum=0
for i in range(0,length):
      a=num%10
      num=num//10
      sum+=a
print(sum)
