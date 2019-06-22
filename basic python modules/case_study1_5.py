'''
Please   write   a   program   which   accepts  a   string   from   console
 and   print   the characters that have even indexes.
 Example: If the following string is given as input to the
  program:H1e2l3l4o5w6o7r8l9d
  Then,
   the output of the program should be:Helloworld
'''


a = input("please put in your string          ")

b=list(a)

for i in b:
    index_number = b.index(i)

    if(index_number%2==0):
        print(i, end='')