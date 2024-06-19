#Program that copies the contents of one text file to another

f=open("India.txt",r)
f1=open("INDIA.txt",w)
re=f.read()
f1.write(re)
