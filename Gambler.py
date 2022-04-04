'''
@Author: Nayan Tripathi
@Date: 2022-03-30 10:00:00
@Title : Gambler
'''

import random
class Gamble:
    def Gambler():
        bet = stake = 1
        goal = 100
        win = loss = total = 0
        while stake <= goal or stake == 0 :
            if random.randint(0,1)==1:
                win +=1
                stake += bet
                print("Stake: ", stake)
                if(stake == goal):
                     break
            else:
                loss += 1
                stake -= bet
                print("Stake: " , stake)
                if(stake == 0):
                    break
        total = win+loss
        print("Win percentage:" ,float(win/total )*100)
        print("Loss percentage",float(loss/total)*100)
    
obj=Gamble
obj.Gambler()