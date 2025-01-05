'''
the following program will print the given pattern :

if n=4

   A
  ABA
 ABCBA
ABCDCBA

the pattern is dynamic which means that it can work for most of the number

chr() -> to convert ascii code into character
ord() -> to convert character into ascii

Happy Coding ;)

'''

def Pattern(n):
    for i in range(n):
        #spaces
        for sp in range(n-1-i):
            print(" ",end="")
        for j in range(i+1):
            print(chr(65+j),end="")
        if(i>0):
            for k in range(i,0,-1):
                print(chr(65+(k-1)),end="")
        print()

def printPattern(num):
    if num == 0 :
        print("---------- Program Terminated ----------")
    else:
        Pattern(num)
        print() #change line
        num = int(input("Enter the number of rows or 0 to terminate the program :"))
        printPattern(num)

num = int(input("Enter the number of rows : "))
printPattern(num)