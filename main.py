from tkinter import Tk, Button, Canvas, Label, PhotoImage, messagebox
import pandas
from random import choice
from os.path import isfile

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

timer = None

# ------------------------ Get new word ------------------------------ #


def remove_card():
    '''
    Removes card from the list and saves it for the future.
    '''
    to_learn.remove(random_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv(words_to_learn_file, index=0)
    fetch_card()


def flip_card(translation=''):
    '''
    Flips the card and showing the translation
    :param translation: the word's english translation
    '''
    window.after_cancel(timer)
    canvas_card.itemconfig(card_image, image=green_card_photo)
    canvas_card.itemconfig(text_language, text='English', fill="white")
    canvas_card.itemconfig(text_current_word, text=translation, fill="white")


def fetch_card():
    '''
    Fetch a card, show it and activate the flip timer
    '''
    global timer, random_card
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
btn_yes = Button(image=yes_image, highlightthickness=0, command=remove_card)
btn_yes.grid(row=1, column=1)

# get words from the list
words_df = pandas.read_csv("data/french_words.csv")
to_learn = words_df.to_dict(orient="records")
words_to_learn_file = "data/words_to_learn.csv"
if not isfile(words_to_learn_file):
    words_df = pandas.read_csv("data/french_words.csv")
    words_df.to_csv(words_to_learn_file, index=0)
    to_learn = words_df.to_dict(orient="records")
else:
    try:
        words_df = pandas.read_csv(words_to_learn_file)
        to_learn = words_df.to_dict(orient="records")
    except pandas.errors.EmptyDataError:
        messagebox.showinfo(title="Congrats", message="You have successfully learned all the words")

random_card = None
timer = window.after(3000, flip_card)
fetch_card()

window.mainloop()
