import card

class Player():

    def __init__(self, name = ""):
      self.name = name  
      self.hand = []
    
    def add_card(self, card):
        self.hand.append(card)

    def clear_card(self):
        self.hand = []
