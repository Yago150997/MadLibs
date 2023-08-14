#Let's learn how to concatened strings with madlib

from tkinter import *
from tkinter import ttk
from functools import partial

def show_text(Name, Object, weapon, onomatopeia):

    janela_de_texto = Tk()
    janela_de_texto.title("Text")
    janela_de_texto.geometry("800x600")

    nameText = Name.get()
    ObjectText = Object.get()
    weaponText = weapon.get()
    onomatopeiaText = onomatopeia.get()

    madlib = f"BOOM. They knocked again. {nameText} awake.\
    \nWhere’s the {ObjectText}?” he said stupidly.\
    \nThere was a crash behind them and Uncle Vernon\
    \ncame skidding into the room. He was holding a {weaponText} in\
    \nhis hands — now they knew what had been in the\
    \nlong, thin package he had brought with them.\
    \n“Who’s there?” he shouted. “I warn you — I’m armed!”\
    \nThere was a pause. Then —\
    {onomatopeiaText}!\
    \nThe door was hit with such force that it swung clean\
    \noff its hinges and with a deafening crash landed flat\
    \non the floor."

    text = Label(janela_de_texto, text = madlib, anchor="e", justify="right").grid(column=0, row=0,padx=10, pady=10)
    return


Janela_da_madlib = Tk()
Janela_da_madlib.title("MadLib")
Janela_da_madlib.geometry("800x600")

word1 = Label(Janela_da_madlib, text = "Name: ").grid(column=0, row=0,padx=10, pady=10)
Name = Entry(Janela_da_madlib)
Name.grid(column=1, row=0, padx=10, pady=10)

word2 = Label(Janela_da_madlib, text = "Obejct: ").grid(column=0, row=1,padx=10, pady=10)
Object = Entry(Janela_da_madlib)
Object.grid(column=2, row=1, padx=10, pady=10)

word2 = Label(Janela_da_madlib, text = "Weapon: ").grid(column=0, row=2,padx=10, pady=10)
weapon = Entry(Janela_da_madlib)
weapon.grid(column=1, row=2, padx=10, pady=10)

word2 = Label(Janela_da_madlib, text = "onomatopeia: ").grid(column=0, row=3,padx=10, pady=10)
onomatopeia = Entry(Janela_da_madlib)
onomatopeia.grid(column=1, row=3, padx=10, pady=10)

callTextWindow = partial(show_text, Name, Object, weapon, onomatopeia)

submitButton = Button(Janela_da_madlib, text="submit", command=callTextWindow).grid(column=1, row=4)


Janela_da_madlib.mainloop()