'''
A website requires a user to input username and password to register. Write a program to check the validity of password given by user. Following are the criteria for checking password:1. At least 1 letter between [a-z]2. At least 1 number between [0-9]1. At least 1 letter between [A-Z]3. At least 1 character from [$#@]4. Minimum length of transaction password: 65. Maximum length of transaction password: 12
'''

#password
import re


def check(password):
    if (re.search("^(?=.{6,12}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$",password)):
        exit(0)

    else:
        print("The Password Is Not Correct")
        return 1


val="YES"

while (val=="YES"):
    password = input("Please write the password            ")
    authorize = check(password)
    if(authorize==1):
        rep=input("Do you wish to try your luck again YES/NO                ")
        val=rep

    else:
        val="NO"


