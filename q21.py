#Program that counts the occurrences of a specific element in a list

l=[1,2,5,3,2,2,1,4]
count=0
search=int(input("enter the number you want to count occurences of"))
for i in range(len(l)):
    if l[i]==search:
        count+=1
print(count)
