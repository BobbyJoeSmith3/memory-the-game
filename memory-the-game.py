# implementation of card game - Memory

import simplegui
import random

number_of_pairs = 8
card_list = []
exposed = []
card_width = 50

# helper function to initialize globals
def new_game():
    print card_list
    print exposed

def generate_deck(number_of_pairs):
    #create and concatenate two lists of numbers range 0-8
    global card_list, exposed
    card_list = range(number_of_pairs)
    card_list.extend(range(number_of_pairs))
    #shuffle deck
    random.shuffle(card_list)
    #create exposed card list
    i = 0
    while i < (number_of_pairs * 2):
       exposed.append(False)
       i += 1

# define event handlers
def mouseclick(pos):
    # add game state logic here
    ndx = pos[0] // card_width
    print ndx



# cards are logically 50x100 pixels in size
def draw(canvas):
    global card_width
    card_start = 0
    card_width = 50
    #draw cards
    for card in range(len(card_list)):
        canvas.draw_polygon([(card_start,0), ((card_start + card_width),0),
                       ((card_start + card_width),100), (card_start,100)],
                       1, 'black', 'green')
        #draw the number of the card if the card is exposed
        if exposed[card] == True:
            canvas.draw_text(str(card_list[card]), [card_start, 24], 24, "White")
        #move over a space to draw the next card
        card_start += card_width


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
generate_deck(number_of_pairs)
new_game()
frame.start()


# Always remember to review the grading rubric
