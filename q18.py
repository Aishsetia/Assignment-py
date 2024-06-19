#Program that checks if two strings are anagrams of each other

'''LOGIC-first we store the string letters in the form of elements in a list
then we check if length of both the strings are equal or not.if equal then code
continues otherwise it can't be an anagram.Then a for loop iterates through
elements in the first list and check if that element is in the second list or
not,consequently removing the element from both the list to prevent repitition
of elements.If the element matches with element in list 2 then a=1.If not then
a=2.At the end if all the elements are matched then a=1 hence the strings are
anagrams of each other.'''

string1=str(input("enter a string"))
string2=str(input("enter another string"))
string1.lower()
string2.lower()
l1=list(string1)
l2=list(string2)
if len(l1)==len(l2):
   for i in l1:
       if i in l2:
           print(i)
           l1=l1.remove(i)
           l2=l2.remove(i)
           a=1
       else:
           a=2
else:
    a=2
if a==1:
   print("anagram")
else:
    print("not")

