'''
the following program will print the given pattern :

if n=10 (number of rows)



the pattern is dynamic which means that it can work for most of the number


Happy Coding ;)

'''

def Pattern(n) : 
    for i in range(n):
        for j in range(0,i+1):
            print(i*j,end=" ")
        print()

def patternPrinting(num):
    if num == 0:
        print("---------- Program Terminated ----------")
        return
    else: 
        Pattern(num)
        print()
        num = int(input("Enter the number of rows or 0 to terminate the program: "))
        patternPrinting(num)

num = int(input("Enter the number of rows or 0 to terminate the program: "))
patternPrinting(num)