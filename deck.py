import random
from card import Card
#for card creation.
symbols = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
#card list
holder = []

class Decks():
  #builds a x number of decks
  def deck_build(self , number_of_decks = 1):
    #BUILDS A NUMBER OF COMPLETE VERSIONS OF A COMPLETE DECK.
    for x in range(number_of_decks):
      #t = looks through the value array and gets the face values
      for t in value.keys(): 
        #provides the suit value 
        for s in symbols:
          #add a new card to my list. 
          holder.append(Card(s , t , value[t]))
  #can edit this is where i can edit how many decks i can have
  def __init__(self, number_of_decks = 1):
     self.deck_build(number_of_decks)

  def shuffle_deck(self):
    random.shuffle(holder) 
  #len of holder shows me how many cards in hand. makes sure that a new card is drawn.
  def draw_card(self):
    if len(holder) <= 0:
      #makes sure that the deck is not deplete all the way and adds a new deck.
      self.resupply()
    #new card is drawn and taken out of the deck.
    return(holder.pop())
  #makes a new deck to avoid an error when all 52 cards are used.
  def resupply(self):
    print("new deck")
    self.deck_build()
    self.shuffle_deck()


    
