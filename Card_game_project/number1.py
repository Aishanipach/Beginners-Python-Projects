class Cards:

    def __init__(self, suit, rank):
        self.rank=rank
        self.suit=suit
    
    def __str__(self):
        return self.rank 