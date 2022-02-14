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

WINDOW_NAME = "The Flash"
# generate a window using the tkinter class
window = tkinter.Tk()
# change the name of the window
window.title(WINDOW_NAME)
# set the size of the padding between canvas and the windows
window.config(padx=50, pady=50)
# window.geometry("800x526")
canvas = tkinter.Canvas(width=800, height=526)
# center the window upon opening
window.eval('tk::PlaceWindow . center')
# loop the main window to stay open
window.mainloop()