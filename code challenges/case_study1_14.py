'''

Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
Example:If the following n is given as input to the
program:5
Then, the output of the program should be:3.55
'''


import random

input_val = int(input("Please provide input to the programme"))

a=[]
def cal(input_val):
    if (input_val>0):
        for i in range(1,input_val+1,1):
            b=i/(i+1)
            a.append(b)

        else: print("please provide a valid number greater than 0")

        c=round(sum(a),3)

        return c

value= cal(input_val)

print(value)




