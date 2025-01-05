'''
here's the pattern that the following program will print : 

1. it should work only for odd number
2. for even number program should give a message about 'wrong output' and an retake input from the user.
3. it should be dynamic that it should work for every odd 'n'

if n=3                          
         ee
 *       *
 *   *   *
 *eee*eee*
 *   *   *    
 *       *
ee


if n=5

               eeee
   *           *
   *     *     *
   *     *     *
   *eeeee*eeeee*
   *     *     *
   *     *     *
   *           *
eeee   

'''

def PrintEs(n) :
   for i in range(n) :
      print('e',end="")

def Pattern(n) :
   #part 1
   for i in range(3*n) :
      print(" ",end="")
   PrintEs(n-1)
   print() #change line

   #part 2
   for i in range(n+2):
      #space
      for sp in range(n-2):
         print(" ",end="")
      for j in range(2*n+3):
         if(i==0 or i==n+1):
            if(j>0 and j<(2*n+3)-1):
               print(" ",end="")
            else:
               print('*',end="")
         else:
            if(i==(n+1)/2):
               if(j>0 and j<(2*n+3)-1):
                  if(j==(2*n+2)/2):
                     print('*',end="")
                  else:
                     print("e",end="")
               else :
                  print('*',end="")
            else:
               if(j>0 and j<(2*n+3)-1):
                  if(j==(2*n+2)/2):
                     print('*',end="")
                  else:
                     print(" ",end="")
               else :
                  print('*',end="")
      print()


   #part 3
   PrintEs(n-1)

def checkValid(num):
   if(num == 0):
      print("------------ Program Terminated ------------")
   elif(num%2 == 0):
      print("Wrong Input! Please enter an even number")
      num = int(input("Enter an odd number or enter 0 to exit: "))
      checkValid(num)
   else:
      Pattern(num)

num = int(input("Enter an odd number or enter 0 to exit: "))
checkValid(num)
