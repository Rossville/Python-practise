'''
the following program will print the given pattern :

if n=5 (number of rows)

    1 
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

the pattern is dynamic which means that it can work for most of the number

Happy Coding ;)

'''


def Pattern(num):
    coef = 1
    for i in range(1, num+1):
        for space in range(1, num-i+1):
            print(" ",end="")
        for j in range(0, i):
            if j==0 or i==0:
                coef = 1
            else:
                coef = coef * (i - j)//j
            print(coef, end = " ")
        print()
        

def patternPrinting(num):
    if num == 0:
        print("---------- Program Terminated ----------")
    else: 
        Pattern(num)
        print()
        num = int(input("Enter number of rows or 0 to terminate the program: "))
        patternPrinting(num)
        
num = int(input("Enter number of rows or 0 to terminate the program: "))
patternPrinting(num)