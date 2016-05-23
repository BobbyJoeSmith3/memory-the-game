# implementation of card game - Memory

import simplegui
import random

DECK = []
EXPOSED = []
CARD_WIDTH = 50
CARD_HEIGHT = 100
GAME_STATE = 0
CHOICE1_VALUE = None
CHOICE1_INDEX = None
CHOICE2_VALUE = None
CHOICE2_INDEX = None
TURNS = 0


# helper function to initialize globals
def generate_cards(low_card, high_card):
    global DECK
    high_card = high_card + 1
    list1 = range(low_card, high_card)
    list2 = range(low_card, high_card)
    DECK = list1 + list2
    random.shuffle(DECK)
    # create initial list of which cards are exposed
    num_of_cards = len(DECK)
    for card in range(num_of_cards):
        EXPOSED.append(False)


def new_game():
    global TURNS, DECK

    # reshuffle cards
    random.shuffle(DECK)

    # hide all cards
    num_of_cards = len(DECK)
    for card in range(num_of_cards):
        EXPOSED[card] = False

    # reset turn counter
    TURNS = 0
    label.set_text("Turns = " + str(TURNS))


# define event handlers
def mouseclick(pos):
    global EXPOSED, GAME_STATE, TURNS
    global CHOICE1_VALUE, CHOICE2_VALUE, CHOICE1_INDEX, CHOICE2_INDEX

    # determine which card was clicked
    card_idx = pos[0] // CARD_WIDTH

    # add game state logic here
    # only change game state if card isn't already exposed
    if EXPOSED[card_idx] == False:
        if GAME_STATE == 0:
            # flip card
            EXPOSED[card_idx] = True
            # assign card value to choice 1
            CHOICE1_VALUE = DECK[card_idx]
            # temporarily store card index of choice 1
            CHOICE1_INDEX = card_idx
            # change game state
            GAME_STATE = 1
        elif GAME_STATE == 1:
            # flip card
            EXPOSED[card_idx] = True
            # assign card value to choice 2
            CHOICE2_VALUE = DECK[card_idx]
            # temporarily store card index of choice 2
            CHOICE2_INDEX = card_idx
            # change game state
            GAME_STATE = 2
        else:
            # increment turn counter
            TURNS = TURNS + 1
            label.set_text("Turns = " + str(TURNS))
            # check if cards are the same, if not flip
            if CHOICE1_VALUE != CHOICE2_VALUE:
                # flip cards back over
                EXPOSED[CHOICE1_INDEX] = False
                EXPOSED[CHOICE2_INDEX] = False
            # flip card
            EXPOSED[card_idx] = True
            # assign card value to choice 1
            CHOICE1_VALUE = DECK[card_idx]
            # temporarily store card index of choice 1
            CHOICE1_INDEX = card_idx
            # change game state
            GAME_STATE = 1


# cards are logically 50x100 pixels in size
def draw(canvas):
    # variables for card construction
    text_x = 18
    text_y = 60
    font_size = 24
    card_index = 0
    card_x = 0
    card_y = 0

    # draw cards
    for card_value in DECK:
        canvas.draw_polygon([(card_x, card_y),
                             (card_x + CARD_WIDTH, card_y),
                             (card_x + CARD_WIDTH, card_y + CARD_HEIGHT),
                             (card_x, card_y + CARD_HEIGHT)], 1, 'white', 'green')
        # if card is exposed draw value, otherwise show green card without value
        if EXPOSED[card_index] == True:
            canvas.draw_text(str(card_value),(text_x, text_y), font_size, 'white')

        card_index = card_index + 1
        text_x = text_x + CARD_WIDTH
        card_x = card_x + CARD_WIDTH



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(TURNS))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
generate_cards(0,7)
frame.start()


# Always remember to review the grading rubric
