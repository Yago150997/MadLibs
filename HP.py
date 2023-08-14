#Let's learn how to concatened strings with madlib

# importing the necessaries libraries
from tkinter import *
from tkinter import ttk
from functools import partial

def show_text(Name, Object, weapon, onomatopeia):

    text_window = Tk()
    text_window.title("Text")
    text_window.geometry("800x600")

    nameText = Name.get()
    ObjectText = Object.get()
    weaponText = weapon.get()
    onomatopeiaText = onomatopeia.get()

    madlib = f"BOOM. They knocked again. {nameText} awake.\
    Where’s the {ObjectText}?” he said stupidly.\
    There was a crash behind them and Uncle Vernon\
    came skidding into the room. He was holding a {weaponText} in\
    his hands — now they knew what had been in the\
    long, thin package he had brought with them.\
    “Who’s there?” he shouted. “I warn you — I’m armed!”\
    nThere was a pause. Then —\
    {onomatopeiaText}!\
    nThe door was hit with such force that it swung clean\
    off its hinges and with a deafening crash landed flat\
    on the floor."

    text = Label(text_window, text = madlib, justify="left", wraplength=800).grid(column=0, row=0,padx=10, pady=10)
    return


madlib_window = Tk()
madlib_window.title("MadLib")
madlib_window.geometry("800x600")

word1 = Label(madlib_window, text = "Name: ").grid(column=0, row=0,padx=10, pady=10)
Name = Entry(madlib_window)
Name.grid(column=1, row=0, padx=10, pady=10)

word2 = Label(madlib_window, text = "Obejct: ").grid(column=0, row=1,padx=10, pady=10)
Object = Entry(madlib_window)
Object.grid(column=2, row=1, padx=10, pady=10)

word2 = Label(madlib_window, text = "Weapon: ").grid(column=0, row=2,padx=10, pady=10)
weapon = Entry(madlib_window)
weapon.grid(column=1, row=2, padx=10, pady=10)

word2 = Label(madlib_window, text = "onomatopeia: ").grid(column=0, row=3,padx=10, pady=10)
onomatopeia = Entry(madlib_window)
onomatopeia.grid(column=1, row=3, padx=10, pady=10)

callTextWindow = partial(show_text, Name, Object, weapon, onomatopeia)

submitButton = Button(madlib_window, text="submit", command=callTextWindow).grid(column=1, row=4)


madlib_window.mainloop()