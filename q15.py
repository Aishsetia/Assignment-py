#Program that reads data from a CSV file and prints it

import csv
f=open("India.csv",'r')
read=csv.reader(f)
for i in read:
     print(i)
