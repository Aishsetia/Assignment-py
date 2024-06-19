#Program that takes a list of numbers and returns their sum.

sum=0
l=[]
a=int(input("how many numbers do you want to add"))
for i in range(a):
    num=int(input("enter a number"))
    l.append(num)
for i in l:
    sum+=i
print(sum)
