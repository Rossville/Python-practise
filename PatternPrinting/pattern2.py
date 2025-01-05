'''
the following program will print the given pattern :

1       1
12     21
123   321
1234 4321
123454321

the pattern is dynamic which means that it can work for most of the number

Happy Coding ;)

'''

def Pattern(n):
    for i in range(n):
        #pattern 1
        for j in range(n):
            if(j<=i):
                print(j+1,end="")
            elif(j<n):
                print(" ",end="")
        #space
        for sp in range(n-2-i):
            print(" ",end="")
        #pattern 2
        for k in range(i+1,0,-1):
            if(k<n):
                print(k,end="")
        print()



while(True): 
    num = int(input("Enter a number or enter 0 to terminate the program : "))
    if num == 0:
        print("---------- Program Terminated ----------")
        break
    else:
        Pattern(num)
        print()