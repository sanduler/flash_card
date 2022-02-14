# Ruben Sanduleac

import tkinter
# --------------------------------- UI -----------------
#TODO: user tkinter to build the mainscreen
#TODO: implement the canvas --> where the word and the definition will be placed on the
#TODO: implement the X icon on the mainscreen that the user can click on --> they didnt get it right
#TODO: the x will keep the word/definition in the stack
#TODO: implement the checkmark icon on the mainscreen that the user can click on --> they got it right
#TODO: the checkmark will remove the word/definition from the stack
#TODO: give a background to the mainscreen
#TODO: use the JSON format to store the words/definition from the users data
import background as background

BACKGROUND_COLOR = "#B1DDC6"

WINDOW_NAME = "The Flash"
# generate a window using the tkinter class
window = tkinter.Tk()
# change the name of the window
window.title(WINDOW_NAME)
# set the size of the padding between canvas and the windows
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.geometry("800x526")
canvas = tkinter.Canvas(width=850, height=530)
flash_image = tkinter.PhotoImage(file="./img/card_front.png")
canvas.create_image(420, 270, image=flash_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
right_image = tkinter.PhotoImage(file="./img/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, bd=0)
right_button.grid(column=0, row=1)
wrong_image = tkinter.PhotoImage(file="./img/wrong.png")
wrong_button = tkinter.Button(image=wrong_image)
wrong_button.config(highlightthickness=0, bd=0)
wrong_button.grid(column=1, row=1)
# center the window upon opening
window.eval('tk::PlaceWindow . center')
# loop the main window to stay open
window.mainloop()