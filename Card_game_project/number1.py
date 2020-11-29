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
    
    def add_cards(self,added_cards, name):
        if type(added_cards) == type([]):
            self.deck.extend(added_cards)
        else:
            self.deck.append(added_cards)
        print(f"{name} player has {len(self.deck)} cards")


def main():
    print("\t WELCOME TO the CARD GAME- WAR!\n\n")
    print("Let's shufle,divide and start!")
    d=Create_Deck()
    d.deal_1()
    d.add_cards(["2", "Ace","hey"], "P1")
main()

