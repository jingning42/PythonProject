# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
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
        self.hand = []	# create Hand object
        self.result = ''
       
    def __str__(self):
       return 'Hand contains ' + self.result  	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand
        self.result += str(card) + ' ' 
        
    def get_value(self):
        hand_value = sum(VALUES[str(card)[1]] for card in self.hand) 
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        for card in self.hand:
            if 'A' == card.get_rank():
                if hand_value + 10 <= 21:
                    return hand_value + 10
        return hand_value
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.hand:
            card.draw(canvas, (pos[0]+i*(CARD_SIZE[0]+10), pos[1]))
            i += 1
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))
   
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop(-1)	# deal a card object from the deck
    
    def __str__(self):
        result = ''
        for card in self.deck:
            result += str(card) + ' '
        return 'Deck contains ' + result	# return a string representing the deck


#define event handlers for buttons
def deal():			# deal 是'发牌'的意思 - 同时'洗牌了'
    global outcome, in_play, deck, dealer_hand, player_hand, score
    if in_play == False:
        deck = Deck()
        dealer_hand = Hand()
        player_hand = Hand()
        deck.shuffle()
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        in_play = True
        outcome = ''
    elif in_play == True:
        outcome = 'You lost!'
        score -= 1
        in_play = False
    
def hit():
    global outcome, in_play, deck, dealer_hand, player_hand, score
    if in_play == True:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = 'You have busted. You lost!'
            in_play = False
            score -= 1			# hit是'叫牌'的意思
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, deck, dealer_hand, player_hand, score
    if in_play == True:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = 'Dealer has busted. You win!'
            in_play = False
            score += 1
        elif player_hand.get_value() < dealer_hand.get_value():
            outcome = 'You lost!'
            in_play = False
            score -= 1
        elif player_hand.get_value() > dealer_hand.get_value():
            outcome = 'You win!'
            in_play = False
            score += 1
        else:
            outcome = 'Tie!'
            in_play = False
            
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, in_play, deck, dealer_hand, player_hand, score
    player_hand.draw(canvas, [100, 300])
    dealer_hand.draw(canvas, [100, 100])
    canvas.draw_text('Blackjack', [80, 60], 40, 'White')
    canvas.draw_text(outcome, [100, 500], 33, 'White')
    canvas.draw_text('score:'+str(score), [400, 60], 40, 'White')
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE , [100 + CARD_CENTER[0], 100 + CARD_CENTER[1]], CARD_BACK_SIZE)
        canvas.draw_text('Hit or stand?', [100, 260], 35, 'White')
    elif in_play == False:
        canvas.draw_text('New deal?', [100, 260], 40, 'White')
    
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

# remember to review the gradic rubric