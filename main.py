#imports
from deck import Decks
from player import Player

#start game function holds my inputs for the player's name and starts the game
def start_game():
    name = input("Enter your name: ")
    print("")
    introduction = input("Welcome to The Tops Casino, {}! You here for some Blackjack? (Yes or No) \n".format(name))
    print("")
    if introduction == "Yes" or "yes":
        start(name)
    elif introduction == "No" or "no":
        print("Game Over!")

#start function begins the main loop for the game
def start(name):
    #variables for the game. blackjack uses 4 decks
    deck = Decks(4)
    #main player variables
    player = Player(name)
    dealer = Player("House")
    #while loop switch. always true until the game is over (false)
    playing = True
    #how I randomize my deck
    deck.shuffle_deck()
    #player draws two cards
    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())
    #dealer draws one deck
    dealer.add_card(deck.draw_card())
    #main game loop.
    while playing:
        
        print("Your hand holds the:")
        #this displays what cards the player has
        show(player.hand)
        #this shows the number value of your cards so you dont have to count :)
        print("Hand Value: ", total(player.hand))
        #win condition to return certain outcomes (win or lose or none)
        #win = True
        #lose = False
        #keep playing = None
        win = win_condition(player)
        #if the win condition (getting a 21) is not met the player continues playing (hit or stay)
        if win == None:
            
            print("")
            
            print("The dealer has:")
           
            show(dealer.hand)
            #i placed this input here to provide a chance for the player to stay or draw another card.
            choice = input("Please enter H for hit or S for stay: ")
            #when player inputs H then the hit function will have the player draw another card
            if choice == "H":
                hit(deck , player)
            #when player inputs S then the stay function will play the secondary loop for dealer to play their hand
            elif choice == "S":
                playing = stay(deck, player , dealer)
            else:
                print("Error. Please type H or S.")
        
        elif win == True:
            print("")
            print("YOU WIN.")
            playing = new_game(deck, player , dealer)
        else:
            print("")
            print("YOU LOSE.")
            playing = new_game(deck, player, dealer)
    
    print("Happy Trails!")
    
    
def total(hand):
    hand_value = 0
   #sorts the hand. i sorted the hand value to help me determine the value of Ace since ace can be either lowest or highest value depending on the other cards
    for card in sorted(hand, key=lambda card: card.value):
        if card.face == "Ace":
            if hand_value + 11 <= 21:
                hand_value = 11 + hand_value
            else: 
                hand_value = 1 + hand_value
        else:
            hand_value = card.value + hand_value
    return hand_value

def show(hand):
    for card in hand:
        print (card.display_card())
        
def hit(deck , p):
    p.add_card(deck.draw_card())

def stay(deck, p , d):
    playing = True
    while playing:

        print("")

        print("The dealer has:")

        show(d.hand)

        print("Hand Value: ", total(d.hand))

        print("")
        #introduced the dealer's win condition.
        dwin = dealer_win_con(p, d)

        if dwin == None:
            hit(deck, d)
        elif dwin == True:
            print("HOUSE WINS.")
            return new_game(deck, p , d)
        else:
            print("YOU WIN.")
            return new_game(deck, p , d)
    return False


def win_condition(p):
    t = total(p.hand)
    if t == 21:
        return True
    elif t > 21:
        return False
    else:
        return None


def dealer_win_con(p , d):
    td = total(d.hand)
    tp = total(p.hand)
    if td == 21 or (td > tp and td <= 21):
        return True
    elif td > 21:
        return False
    else: 
        return None
#function to restart the game  
def new_game(deck , p , d):
    print("")
    n_game = input("Play again? Enter Yes or No: ")
    print("")
    
    if n_game == "Yes" or "yes":
        #need to clear the hand to introduce new cards 
        p.clear_card()
        d.clear_card()
        #introduced new cards to both players
        p.add_card(deck.draw_card())
        p.add_card(deck.draw_card())
        d.add_card(deck.draw_card())
        #True restarts the playing loop
        return True
    else:
        #False ends the loop. good sub for a break
        return False   
#function to begin the game
start_game()