# Ruben Sanduleac

import tkinter
import pandas
import random

# --------------------------------- UI -----------------
# TODO: implement the canvas --> where the word and the definition will be placed on the
# TODO: implement the X icon on the mainscreen that the user can click on --> they didnt get it right
# TODO: the x will keep the word/definition in the stack
# TODO: implement the checkmark icon on the mainscreen that the user can click on --> they got it right
# TODO: the checkmark will remove the word/definition from the stack
# TODO: give a background to the mainscreen
# TODO: use the JSON format to store the words/definition from the users data

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_NAME = "The Flash"
DATA_WORDS = pandas.read_csv("data/french_words.csv")
learn_words = DATA_WORDS.to_dict(orient="records")

# def start_timer():
#     """This function is responsible for
#     the response from the button click"""
#     global reps
#     # increment the reps with each change
#     reps += 1
#
#     work_sec = WORK_MIN
#     short_break_sec = SHORT_BREAK_MIN
#     long_break_sec = LONG_BREAK_MIN
#
#     # if there are 8 reps then we take a long 20 minute break
#     if reps % 8 == 0:
#         count_down(long_break_sec * 60)
#     # every two reps we take a 5 minute break
#     elif reps % 2 == 0:
#         timer_rest()
#         count_down(short_break_sec * 60)
#     # else we work
#     else:
#         timer_work()
#         count_down(work_sec * 60)


# def count_down(count):
#     global TIMER
#     # count = 3
#     if count > 0:
#         # we loop recursifly through the function
#         timer = window.after(1000, count_down, count - 1)
#         back_image = tkinter.PhotoImage(file="./img/card_back.png")
#         canvas.create_image(420, 270, image=back_image)
#         canvas.grid(column=0, row=0, columnspan=2)
CURRENT_CARDS = {}


def flip_card():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=CURRENT_CARDS["English"])


def new_word():
    global CURRENT_CARDS
    CURRENT_CARDS = random.choice(learn_words)
    french_word = (CURRENT_CARDS["French"])
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=french_word)


# generate a window using the tkinter class
window = tkinter.Tk()
# change the name of the window
window.title(WINDOW_NAME)
# set the size of the padding between canvas and the windows
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(4000, func=flip_card)
# window.geometry("800x526")
canvas = tkinter.Canvas(width=850, height=530)
flash_image = tkinter.PhotoImage(file="./img/card_front.png")
# # back_image = tkinter.PhotoImage(file="./img/card_back.png")
canvas.create_image(420, 270, image=flash_image)
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
