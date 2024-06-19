#Program that converts temperature from Celsius to Fahrenheit and vice versa

'''FORMULA=°F = (9/5) * °C + 32
           °C = (5/9) * (°F - 32)'''

y=int(input("enter 1 if conversion to Fahrenheit or 2 for Celsius"))
if y==1:
   c=int(input("enter temperature in Celsius"))
   f=9/5 *c +32
   print(f)
else:
    f=int(input("enter temperature in Fahrenheit"))
    c=5/9*(f-32)
    print(c)
    

