'''Case Study II - Verification and Encryption of Reference ID'''

import re
from cryptography.fernet import Fernet



def check_validity(user_input):
    if(re.search("^(?=.{12,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W).*$",user_input)):
        return 0
    else:
        print("input is not in correct order")
        return -1




def encryp(user_input):
    key = Fernet.generate_key()
    #print("key is ",key)
    f = Fernet(key)
    #print("f is " ,f)
    encoded_val=user_input.encode()
    #print(encoded_val)
    token= f.encrypt(encoded_val)
    #print("token is ",token)
    return token,key

def decry(token,key):
    f= Fernet(key)
    value=f.decrypt(token)
    return value


if __name__ == "__main__":

    check = "YES"

    while(check=="YES"):

        user_input=input("Please type in your reff id")

        token=''
        ch = check_validity(user_input)
        #print(ch)

        if (ch==-1):

            check=input("incorrect reff.id do you wish to continue   YES/NO        ")


        else:
            encryption_token, encryption_key = encryp(user_input)
            print(encryption_token, encryption_key)

            val = input("do you wish to decrypt the reff. id. YES/NO")

            if (val == "YES"):
                decrypted_value = decry(encryption_token, encryption_key)

                print(decrypted_value)

            check="NO"


