# Name: Ruben Sanduleac

import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_NAME = "The Flash"
TIMER = 2000
LEARN_WORDS = {}
CURRENT_CARDS = {}

try:
    DATA_WORDS = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    LEARN_WORDS = original_data.to_dict(orient="records")
else:
    LEARN_WORDS = DATA_WORDS.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=CURRENT_CARDS["English"])
    canvas.itemconfig(card_background, image=back_image)
    window.after(TIMER, func=flip_card)


def new_word():
    global CURRENT_CARDS, flip_timer
    window.after_cancel(flip_timer)
    CURRENT_CARDS = random.choice(LEARN_WORDS)
    french_word = (CURRENT_CARDS["French"])
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word)
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(TIMER, func=flip_card)


def is_known():
    LEARN_WORDS.remove(CURRENT_CARDS)
    data = pandas.DataFrame(LEARN_WORDS)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_word()


def ui_buttons(correct_image, incorrect_image):
    right_button = tkinter.Button(image=correct_image, highlightthickness=0, bd=0, command=is_known)
    right_button.grid(column=0, row=1)
    wrong_button = tkinter.Button(image=incorrect_image, command=new_word)
    wrong_button.config(highlightthickness=0, bd=0)
    wrong_button.grid(column=1, row=1)


# generate a window using the tkinter class
window = tkinter.Tk()
# change the name of the window
window.title(WINDOW_NAME)
# set the size of the padding between canvas and the windows
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# create a timer to flip the card
flip_timer = window.after(TIMER, func=flip_card)
# window.geometry("800x526")
canvas = tkinter.Canvas(width=850, height=530)
# Front and back images for the flashcards
front_image = tkinter.PhotoImage(file="./img/card_front.png")
back_image = tkinter.PhotoImage(file="./img/card_back.png")
# create the size for the card background
card_background = canvas.create_image(420, 270, image=front_image)
# config the initial background color for the canvas
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# place the canvas object on the screen
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
new_word()
# pull the two images for the button and pass them into the ui_buttons function
right_image = tkinter.PhotoImage(file="./img/right.png")
wrong_image = tkinter.PhotoImage(file="./img/wrong.png")
ui_buttons(right_image, wrong_image)
# center the window upon opening
window.eval('tk::PlaceWindow . center')
# loop the main window to stay open
window.mainloop()
