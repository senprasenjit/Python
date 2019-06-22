'''Please  write  a  program  to  randomly  generate  a
 list  with  5  numbers,  which  are divisible by 5 and 7 , between 1 and 1000 inclusive'''

import random


a=[]

def calculate(x,y):


    for i in range(x,y,1):
       if(i%5==0 and i%7==0):
           a.append(i)

       else : continue

    ran1 = random.sample(a,5)
    return ran1



calling = calculate(1,1000)
#print(a) [455, 245, 910, 105, 980]
print(calling)
