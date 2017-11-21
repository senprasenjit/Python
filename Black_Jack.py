import sys
import random

import math

dic_values= {"K":10,"Q":10,"J":10,"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}

list_cards1=list(dic_values.keys())
list_cards2=list(dic_values.keys())
list_cards3=list(dic_values.keys())
list_cards4=list(dic_values.keys())

card_number_user = []
card_number_com = []
com_val= 0
user_val = 0

total_list_card = list_cards1+list_cards2+list_cards3+list_cards4
#print(total_list_card)

class face_value_of_card(object):
    def __index__(self,face_value):
        self.face_value=face_value

    def values(self,value):

        v = []
        t = 0
        for x1 in value:

            v.append(dic_values.get(x1))

        #print(v)

        t = sum(v)
        """
        for x2 in v:
            t += int(v)"""



        return t
        # single value would be passed each time and output should be a dictionary (I think)

        #def output_of_face_value(self):

"""def random_card_met(self):
    card_number_user = random.choice(total_list_card)
    card_number_com = random.choice(total_list_card)
    print(card_number_com)
    print(card_number_user)
    #return  self.card_number_com
    return {"KC": self.card_number_com , "KU" :self.card_number_user}"""




class person(object):
    initial_money=1000

    def __index__(self,initial_money):
        self.initial_money=initial_money

    """def setInitialMoney(self,initial_money):
        self.initial_money=initial_money

    def getInitialMoney(self):
        return int(self.initial_money)"""

    def at2_money_win(self,win_money):
        #print("win mein ",self.initial_money)
        self.initial_money= (int(self.initial_money)- int(win_money))+int(win_money)*2
#        win_money=int(win_money)*2+ (int(self.initial_money) - int(win_money))
        #print("win moey i s",win_money)
        #print("self money is ",(self.initial_money))

      #  return int(win_money)


    def at3_loose_money(self,loose_money):
        #print("loose mein ")
        print(self.initial_money)
        self.initial_money= int(self.initial_money) -  int(loose_money)
  #      loose_money=int(self.initial_money)- int(loose_money)
        #print( "self.money",self.initial_money)
        #print("loose money is ",loose_money)
       # return int(loose_money)

def start_Game():
    print("Lets's start the GAME called BLACKJACK.")
    print("May all the odd be in your favour.")
#    start_stop = input("Please enter one of the options : START or  STOP")
    p1=input("How much money do you have in total")

    p = person()
    p.initial_money=int(p1)
    print("Your Initial Money is: ",p.initial_money)

    con="YES"

    while (con=="YES"):
        #p.InitialMoney(p.getInitialMoney())

        #print(p.initial_money)
        value_of_input=input("Please place a desirable amount to start the BET")
        if value_of_input !=0 or value_of_input is not None:

            #person.initial_money=value_of_input

            print(p.initial_money)
            if int(p.initial_money)>0:
                print("We are starting the game.")
                card_number_user = random.sample(total_list_card,2)
                card_number_com = random.sample(total_list_card,2)
                for x in card_number_user:
                    total_list_card.remove(x)
            #total_list_card.remove(card_number_user)
                for y in card_number_com:
                    total_list_card.remove(y)
            #total_list_card.remove(card_number_com)
                #print(card_number_com)
                print(card_number_user)
                #print(total_list_card)

        selection_of_user=input("Please select one of the following options :     1: HIT     2: STAND")


        if int(selection_of_user) == 1:
            print("You have selected to HIT")

            fv = face_value_of_card()
            com_val=fv.values(card_number_com)
            user_val = fv.values(card_number_user)

            #print(com_val)
            print("Your current/initial face value of all the cards is : ",user_val)

            if (int(com_val)==21):
                print("Computer has WON the set.")

            elif (int(user_val)==21):
                print("User has WON the game ")

            else:
                co = random.sample(total_list_card,1)
                us = random.sample(total_list_card,1)
                for a in co:
                    card_number_user.append(str(a))
                for b in us:
                    card_number_com.append(b)

                #print(card_number_com)
                print("Your cards after hiting are  : ",card_number_user)

                com_val=fv.values(card_number_com)
                user_val = fv.values(card_number_user)

                #print("Computer's final face value is : ",com_val)
                print("Your final face value of card is :  ",user_val)

                if (int(com_val)>21 and int(user_val)>21  or ((int(com_val)==21) and (int(user_val)==21))) :

                    print("Computer's final face value is : ",com_val)
                    print("Your final face value of card is :  ",user_val)

                    print("Both COM and USER met a draw")
                    print("your net worth remaining is : ", p.initial_money)


                elif (int(com_val)>21):
                    print("Computer's final face value is : ",com_val)
                    print("Your final face value of card is :  ",user_val)

                    print("USER is the WInner.")
                    print(value_of_input)

                    p.at2_money_win(value_of_input)
                    print("your net worth remaining is : ", p.initial_money)

                    #print(p.initial_money)

                elif (int(user_val)>21):
                    print("Computer's final face value is : ",com_val)
                    print("Your final face value of card is :  ",user_val)

                    print("COM is the winner ")


                    p.at3_loose_money(value_of_input)
                    print("your net worth remaining is : ", p.initial_money)

                    #print(p.initial_money)

                elif (int(user_val)>int(com_val)):
                    print("Computer's final face value is : ",com_val)
                    print("Your final face value of card is :  ",user_val)

                    print("USER is the WInner.")
                    print(value_of_input)

                    p.at2_money_win(value_of_input)
                    print("your net worth remaining is : ", p.initial_money)

                    #print(p.initial_money)
                elif (int(user_val)<int(com_val)):
                    print("Computer's final face value is : ",com_val)
                    print("Your final face value of card is :  ",user_val)
                    print("COM is the winner ")


                    p.at3_loose_money(value_of_input)
                    print("your net worth remaining is : ", p.initial_money)

                    #print(p.initial_money)











        elif int(selection_of_user) == 2:
            print("You have selected to STAND")
            fv = face_value_of_card()
            com_val=fv.values(card_number_com)
            user_val = fv.values(card_number_user)
            print("Computer's final face value is : ",com_val)
            print("Your final face value of card is :  ",user_val)

            if (int(com_val)>int(user_val)):
                print("COM has won")

                p.at3_loose_money(value_of_input)

                print("Your net worth remaining is : ",p.initial_money)

            if(int(user_val)>int(com_val)):
                print("USER has won")
                p2=person()
                p.at2_money_win(value_of_input)

                print("your net worth remaining is : ", p.initial_money)

                print(p.initial_money)

            print(com_val)
            print(user_val)


        con=input("Do you wish to continue or quit : YES  NO")




            #print(random_cards.random_card_met())




        # print(value_of_input)


if __name__== "__main__":
    start_Game()