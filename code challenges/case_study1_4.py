'''
Write a for loop that prints all elements of a list and their position in the list.a = [4,7,3,2,5,9]

'''

a = [4,7,3,2,5,9]

b= {}

for a1 in a:
    b[a1]= a.index(a1)

print(b)
