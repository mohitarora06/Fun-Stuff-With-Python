#http://www.codeskulptor.org/#user40_mjDJy0NwdZ_14.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
            # create Hand object
        self.cards = []

    def __str__(self):
            # return a string representation of a hand
        value = ""
        for i in range(len(self.cards)):
            value += " " + str(self.cards[i].get_suit()) + str(self.cards[i].get_rank())
        return "Hand contains " + value 
    def add_card(self, card):
            # add a card object to a hand
            self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
        total_value = 0
        count = 0
        for i in range(len(self.cards)):
            card_rank = self.cards[i].get_rank()
            if VALUES.has_key(card_rank):
                if card_rank == "A":
                    count += 1   
                else:
                    total_value += VALUES[card_rank]
            else:
                print "Wrong Card"
        if count > 0:
            if count == 1:
                total_value += 11
                if total_value > 21:
                    total_value = total_value -10
            elif count == 2:
                total_value += 11
                if total_value > 21:
                    total_value = total_value - 9
                else:
                    total_value += 1
        return total_value
    
    def draw(self, canvas, pos):
        if self == player:
            for i in range(len(self.cards)):
                self.cards[i].draw(canvas, [(i+1)*100, 400])
        elif self == dealer:
            for i in range(len(self.cards)):
                if in_play:
                    if i == 0:
                        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
                    else:
                        self.cards[i].draw(canvas, [(i+1)*100, 200])
                else:
                    self.cards[i].draw(canvas, [(i+1)*100, 200])
            
                
        
# define deck class 
class Deck:
    def __init__(self):
            # create a Deck object
            self.deck = []
            for i in range(len(SUITS)):
                for j in range(len(RANKS)):
                    card = Card(SUITS[i], RANKS[j])
                    self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        card = random.choice(self.deck)
        return card
    string = ""    
    def __str__(self):
        # return a string representing the deck
        for i in range(len(self.deck)):
            string += " " + self.deck[i].get_suit() + self.deck[i].get_rank()
        return "Deck contains " + string

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, score
    
    # intializing player and dealer and deck
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    if in_play:
        score -= 1
    else:
        in_play = True
        
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

def hit():
    global player, deck, in_play, outcome, score, dealer
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    if in_play:
        player_value = player.get_value()
        if player_value < 21:
            player.add_card(deck.deal_card())
            if player.get_value() > 21:
                outcome =  "You went bust and lose"
                score -= 1
                in_play = False
            elif player.get_value() == 21:
                if dealer.get_value() == 21:
                    outcome = "Dealer won"
                    in_play = False
                    score -= 1
                else:
                    outcome = "You Won"
                    in_play = False
                    score += 1
                    
        elif player.get_value() == 21:
            if dealer.get_value() == 21:
                outcome = "Dealer won"
                in_play = False
                score -= 1
            else:
                outcome = "You Won"
                in_play = False
                score += 1

                       

def stand():
    global dealer, deck, in_play, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play:
        in_play = False
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "Dealer went bust and lose"
            score += 1
        else:
            if player.get_value() > dealer.get_value():
                outcome = "Player wins"
                score += 1
            else:
                outcome = "Dealer wins"
                score -= 1
    elif player.get_value() > 21:
        outcome = "You have busted"
    

# draw handler    
def draw(canvas):

    global in_play, outcome, score
    canvas.draw_text('Blackjack', [250, 50], 50, 'Red')
    canvas.draw_text('Dealer', [100, 190], 30, 'Black')
    dealer.draw(canvas, [100, 200])
    canvas.draw_text('Player', [100, 390], 30, 'Black')
    player.draw(canvas, [100, 400])
    
    canvas.draw_text('Score= ' + str(score), [400, 100], 30, 'Black')
    if in_play:
        canvas.draw_text('Hit Or Stand', [250, 390], 30, 'Black')
    else:
        canvas.draw_text('New Deal?', [250, 390], 30, 'Black')
        canvas.draw_text(outcome, [250, 190], 30, 'Black')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


