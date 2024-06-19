#Program that acts as a simple calculator. It should take two
#numbers and an operator (+, -, *, /) as input and print the result

num1=int(input("enter a number"))
num2=int(input("enter a number"))
operator=input("enter operand")

if operator=='+':
    output=num1+num2
elif operator=='-':
    output=num1-num2
elif operator=='*':
     output=num1*num2
else:
    output=num1/num2
print(output)
     
print(output)
