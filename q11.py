#Program that generates the first n numbers in the Fibonacci sequence

'''Fibonacci sequence-The Fibonacci sequence is a sequence of numbers where
   each number is the sum of the two preceding ones. 

LOGIC-first we initialise and print out 0 and 1 i.e. the first two elements
of the sequence and then in the loop we print the sum of the first two elements
and then assign the value of b to a and the value of sum to b so that we keep
printing the next element as the sum of the previous two elements'''

n=int(input("enter value of n"))
a,b=0,1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a,b=b,c
