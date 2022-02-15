from tkinter import Tk, Button, Canvas, Label, PhotoImage

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

window = Tk()
window.title("Flashy")
window.config(width=800, height=526, padx=50, pady=50, bg=BACKGROUND_COLOR)

white_card_photo = PhotoImage(file="images/card_front.png")
green_card_photo = PhotoImage(file="images/card_back.png")

# Canvas

language = "French"
current_word = "trouve"

canvas_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card.create_image(400, 263, image=white_card_photo)
canvas_card.grid(row=0, column=0, columnspan=2)

canvas_card.create_text(400, 150, tex=language, font=LANGUAGE_FONT)
canvas_card.create_text(400, 263, tex=current_word, font=WORD_FONT)

# Buttons

no_image = PhotoImage(file="images/wrong.png")
yes_image = PhotoImage(file="images/right.png")

btn_no = Button(image=no_image, highlightthickness=0)
btn_no.grid(row=1, column=0)
btn_yes = Button(image=yes_image, highlightthickness=0)
btn_yes.grid(row=1, column=1)

window.mainloop()

