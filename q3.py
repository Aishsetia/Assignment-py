#Program to calculate factorial of a number

'''LOGIC-Loop will run with decreasing values of i as step value is -1.Each time
the loop runs value of i gets multiplied and stored in a variable'''

fnum=int(input("enter a number"))
fact=1
for i in range(fnum,0,-1):
    fact*=i
print("factorial of number is",fact)
