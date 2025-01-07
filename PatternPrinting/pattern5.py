'''
the following program will print the given pattern :

if n=10 (number of rows)

0 
0 1
0 2 4
0 3 6 9
0 4 8 12 16
0 5 10 15 20 25
0 6 12 18 24 30 36
0 7 14 21 28 35 42 49
0 8 16 24 32 40 48 56 64
0 9 18 27 36 45 54 63 72 81


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