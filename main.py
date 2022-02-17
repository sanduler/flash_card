# Ruben Sanduleac

import tkinter
import pandas
import random

# --------------------------------- UI -----------------
# TODO: the checkmark will remove the word/definition from the stack
# TODO: give a background to the mainscreen
# TODO: use the JSON format to store the words/definition from the users data

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_NAME = "The Flash"
TIMER = 2000
DATA_WORDS = pandas.read_csv("data/french_words.csv")
learn_words = DATA_WORDS.to_dict(orient="records")
CURRENT_CARDS = {}


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=CURRENT_CARDS["English"])
    canvas.itemconfig(card_background, image=back_image)
    window.after(TIMER, func=flip_card)


def new_word():
    global CURRENT_CARDS, flip_timer
    window.after_cancel(flip_timer)
    CURRENT_CARDS = random.choice(learn_words)
    french_word = (CURRENT_CARDS["French"])
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word)
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(TIMER, func=flip_card)


# generate a window using the tkinter class
window = tkinter.Tk()
# change the name of the window
window.title(WINDOW_NAME)
# set the size of the padding between canvas and the windows
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIMER, func=flip_card)
# window.geometry("800x526")
canvas = tkinter.Canvas(width=850, height=530)
front_image = tkinter.PhotoImage(file="./img/card_front.png")
back_image = tkinter.PhotoImage(file="./img/card_back.png")
card_background = canvas.create_image(420, 270, image=front_image)
# count_down(3)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
right_image = tkinter.PhotoImage(file="./img/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, bd=0, command=new_word)
right_button.grid(column=0, row=1)
wrong_image = tkinter.PhotoImage(file="./img/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, command=new_word)
wrong_button.config(highlightthickness=0, bd=0)
wrong_button.grid(column=1, row=1)
new_word()
# center the word
# center the window upon opening
window.eval('tk::PlaceWindow . center')
# loop the main window to stay open
window.mainloop()
