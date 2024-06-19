#Program that returns the minimum and maximum values in a list of numbers

'''LOGIC-first we assign the value of first element of the list to minv and maxv
considering them to be the minimum or maximum values respectively.Then a loop
is run in which if the element of the list  is less than minv(the first element)
value of this element replaces or gets reassigned to the minv variable.'''

l=[9,8,5,2,9,7]
minv=l[0]
l1=l.copy()
for i in l:
    if i<minv:
        minv=i
print(minv)
maxv=l1[0]
for j in l1:
    if j>maxv:
        maxv=j
print(maxv)
    
