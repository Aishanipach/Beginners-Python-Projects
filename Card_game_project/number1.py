cards=["Ace", "King", "Queen", "Jack", "One", "Two", "Three", "Four", "Five",
             "Six", "Seven", "Eight", "Nine", "Ten"]
suits=["Heart", "Spade", "Diamond","Club"]

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

def main():
     print("\t WELCOME TO the CARD GAME- WAR!\n\n")
     print("Let's shufle,divide and start!")
     ioeck= Create_Deck()
     print(ioeck.deck[1].suit)

main()
