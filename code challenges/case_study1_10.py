'''By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]'''

a= [12,24,35,24,88,120,155]

b = [ i for i in a if i!=24 ]

print(b)