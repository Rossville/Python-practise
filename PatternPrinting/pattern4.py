'''
the following program will print the given pattern :

if n=5

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

the pattern is dynamic which means that it can work for most of the number


Happy Coding ;)

'''

def Patter1(n):
    for i in range(n):
        for j in range(n):
            if(j<=i):
                print('*',end="")
            else:
                print(" ",end="")
        #space
        for sp in range(n-1-i):
                print(" ",end="")

        for k in range(i+1,0,-1):
            print("*",end="")
        print()

def Pattern2(n):
    for i in range(n-1,0,-1):
        for j in range(n):
            if(j<=i-1):
                print('*',end="")
            else:
                print(" ",end="")

        for sp in range(n-i):
            print(" ",end="")

        for k in range(i):
                print('*',end="")
        print()


def printPattern(num):
    if num == 0 :
        print("---------- Program Terminated ----------")
        return
    else:
        Patter1(num)
        Pattern2(num)
        printPattern(int(input("Enter the number or 0 to terminate the program : ")))


num = int(input("Enter the nummber or 0 to terminate the program : "))
printPattern(num)