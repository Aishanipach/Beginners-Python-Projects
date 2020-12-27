from tkinter import *
import tkinter.messagebox
import random 

cards=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits=("Heart", "Spade", "Diamond","Club")

points={"Ace":14, "King":13, "Queen":12, "Jack":11, "One":1, "Two":2, "Three":3, "Four":4, "Five":5,
             "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10}

class Cards:

    def __init__(self, suit, rank):
        self.rank=rank
        self.suit=suit
        self.pts=points[rank]
    
    def __str__(self):
        return self.rank 

class Create_Deck:
    def __init__(self):
        self.deck=[]

        for suit in suits:
            for card in cards:
                new_card=Cards(suit, card)
                self.deck.append(new_card)

        random.shuffle(self.deck) #shuffled the created deck

    def deal_1(self):
        return self.deck.pop()
    
   
    def split_deck(self):   
        d1=[]
        d2=[]
        for x in range(26):
            d1.append(self.deal_1())
            d2.append(self.deal_1())
        
        return d1, d2

class Gameplay:

    def __init__(self, name,deck):
        self.name=name
        self.deck=deck
    
    def draw(self):
        return self.deck.pop()
        

    def add_cards(self,added_cards):
        if type(added_cards) == type([]):
            self.deck.extend(added_cards)
        else:
            self.deck.append(added_cards)
        print(f"{self.name} player has {len(self.deck)} cards")
    
def check_value(card):
    return( points[card])

def main():

    switchup=False
    root = Tk()
    w = Label(root, text=" Card Game !")
    k = Button(root,activebackground="black", text= "Hi")

    #Turn ON & Turn OFF, Volume, Channel UP &DOWN
    rightFrame = Frame(root, width=300, height = 600)
    rightFrame.grid(row=0, column=1, padx=5, pady=2)

    circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
    circleCanvas.grid(row=0, column=0, padx=10, pady=2)
            
    btFrame = Frame(rightFrame, width=200, height = 400)
    btFrame.grid(row=1, column=0, padx=10, pady=2)
    gameLog = Text(rightFrame, width = 25, height = 20, takefocus=0)
    gameLog.grid(row=2, column=0, padx=10, pady=2)

    def check_status(switchup):
        if(switchup==False):
            circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='grey')
            gameLog.grid(row=2, column=0, padx=10, pady=2)
        else:
            circleCanvas.create_oval(20, 20, 80, 80, width=0, fill='red')
            gameLog.grid(row=2, column=0, padx=10, pady=2)  
              

    
    

    #Left frame
    leftFrame = Frame(root, width=600, height = 600)
    leftFrame.grid(row=0, column=0, padx=10, pady=2)
    btnLog = Text(leftFrame, width =25, height = 20, takefocus=0)
    btnLog.grid(row=1, column=0, padx=10, pady=2)
    
    lbl = Label( leftFrame, width =18, height = 1,text=" ^ WAR rounds' log ^ ")
    
    lbl.grid(row=2, column=0, padx=10, pady=2)
    
    
    print("\t WELCOME TO the CARD GAME- WAR!\n\n")
    print("Let's shufle,divide and start!") 
    d=Create_Deck()
    play1, play2= d.split_deck()
    p1=Gameplay("Player 1", play1)
    p2=Gameplay("Player 2", play2)
    
    
    def Game():
        outcome=False
        check_status(True)    
        while(outcome==False):
            if(len(p1.deck)==0):
                gameLog.insert(0.0, "Player 1 is out of cards\n")
                gameLog.insert(0.0,"PLAYER 2 WINS!\n\n" )
                outcome=True
                break
            elif(len(p2.deck)==0):
                gameLog.insert(0.0, "Player 2 is out of cards\n")
                gameLog.insert(0.0,"PLAYER 1 WINS!\n\n" )
                outcome=True
                break
            card1=str(p1.draw())
            card2=str(p2.draw())

            #Check which card has bigger value
            if(check_value(card1)>check_value(card2)):
                gameLog.insert(0.0,"Player 1 won this round\n" )
                p1.add_cards(card2)
            elif(check_value(card1)<check_value(card2)):
                gameLog.insert(0.0,"Player 2 won this round\n" )
                p2.add_cards(card1)

        #If same value, WAR, draw five cards each
            elif(check_value(card1)==check_value(card2)):
                btnLog.insert(0.0,"\tWAR!\n")
                check_status(True)

                if(len(p1.deck)<5):
                    btnLog.insert(0.0, "Player 1 is out of cards\n")
                    btnLog.insert(0.0,"PLAYER 2 WINS!\n\n" )
                    outcome=True
                    break
                elif(len(p2.deck)<5):
                    btnLog.insert(0.0, "Player 2 is out of cards\n")
                    btnLog.insert(0.0,"PLAYER 1 WINS!\n\n" )
                    outcome=True
                    break
                
                else:
                    round=1
                    while(round>0):
                        if(check_value(str(p1.deck[-1]))>check_value(str(p2.deck[-1]))):
                            #Add cards onto winners pile
                            ctr=0
                            list_won=[]
                            #Pop cards from loser's deck
                            while(ctr<5):
                                ctr=ctr+1
                                i=p2.draw()
                                list_won.append(i)
                                
                            
                            p1.add_cards(list_won)
                            btnLog.insert(0.0,"Player 1 won this round\n")
                            round=round -1
                            break

                        elif(check_value(str(p1.deck[-1]))<check_value(str(p2.deck[-1]))):
                            #Add cards onto winners pile
                            ctr=0
                            list_won=[]
                            #Pop cards from loser's deck
                            while(ctr<5):
                                i=p1.draw()
                                ctr=ctr+1
                                list_won.append(i)
                                
                                
                            p2.add_cards(list_won)
                            btnLog.insert(0.0,"Player 2 won this round\n")
                            round=round-1
                            break

                        elif(check_value(str(p1.deck[-1]))==check_value(str(p2.deck[-1]))):
                            round=+1
                            break
    
    redBtn = Button(btFrame, text="Start", command=Game)
    redBtn.grid(row=0, column=0, padx=10, pady=2)

    root.mainloop()
    w.pack()
    k.pack()
    lbl.pack()   
main()

