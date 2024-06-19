#Program that reads multiple lines of input from the user until they enter an
#empty line,then prints all the lines

statement=[]
while True:
    try:
        line=str(input("enter  a line"))
    except EOFError:
           break
    statement.append(line)
    print(statement)
        
