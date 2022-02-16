from tkinter import Tk, Button, Canvas, Label, PhotoImage
import pandas
from random import choice

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

timer = None

# ------------------------ Get new word ------------------------------ #


def flip_card(translation=''):
    window.after_cancel(timer)
    canvas_card.itemconfig(card_image, image=green_card_photo)
    canvas_card.itemconfig(text_language, text='English', fill="white")
    canvas_card.itemconfig(text_current_word, text=translation, fill="white")


def fetch_card():
    global timer
    window.after_cancel(timer)
    random_card = choice(to_learn)
    random_word = random_card["French"]
    canvas_card.itemconfig(card_image, image=white_card_photo)
    canvas_card.itemconfig(text_language, text="French", fill="black")
    canvas_card.itemconfig(text_current_word, text=random_word, fill="black")
    translation = random_card['English']

    timer = window.after(3000, flip_card, translation)


window = Tk()
window.title("Flashy")
window.config(width=800, height=526, padx=50, pady=50, bg=BACKGROUND_COLOR)

white_card_photo = PhotoImage(file="images/card_front.png")
green_card_photo = PhotoImage(file="images/card_back.png")

# Canvas

canvas_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas_card.create_image(400, 263)
canvas_card.grid(row=0, column=0, columnspan=2)

text_language = canvas_card.create_text(400, 150, font=LANGUAGE_FONT)
text_current_word = canvas_card.create_text(400, 263, font=WORD_FONT)

# Buttons

no_image = PhotoImage(file="images/wrong.png")
yes_image = PhotoImage(file="images/right.png")

btn_no = Button(image=no_image, highlightthickness=0, command=fetch_card)
btn_no.grid(row=1, column=0)
btn_yes = Button(image=yes_image, highlightthickness=0, command=fetch_card)
btn_yes.grid(row=1, column=1)

# get words from the list
words_df = pandas.read_csv("data/french_words.csv")
to_learn = words_df.to_dict(orient="records")

timer = window.after(3000, flip_card)
fetch_card()

window.mainloop()
