# importing the necessaries libraries
import os
from tkinter import *
from tkinter import ttk
from functools import partial

def call_HP_window():
    os.system("python HP.py")
    pass


menu_window = Tk()
menu_window.title("Madlib's game menu")
menu_window.geometry("800x600")

explanation = f"Wealcome to the madlib game! In this game you will choose some words especific to the theme to fill the \
    blanks od the texts. Now, choose the specific text theme you wanna play and enjoy with your friends!"


explanation_text = Label(menu_window, text = explanation, wraplength=800)
explanation_text.grid(column=0, row=0, padx=10, pady=10)

button_HP = Button(menu_window, text = "Harry Potter", command = call_HP_window)
button_HP.grid(column=0, row=1)


menu_window.mainloop()