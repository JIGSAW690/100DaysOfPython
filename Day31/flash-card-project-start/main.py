from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_dict = {}


def flip_cards():
    canvas.itemconfig(canvas_image, image=canvas_back_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

#------------------------------- UI SETUP --------------------------------------------
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_cards)


# CANVAS SETUP
canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_image = PhotoImage(file="C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day31/flash-card-project-start/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=bg_image)
canvas_back_image = PhotoImage(file="C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day31/flash-card-project-start/images/card_back.png")
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

#------------------------------- Setting New Flash Cards --------------------------------------------
try:
    data_frame = pandas.read_csv("C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day31/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day31/flash-card-project-start/data/french_words.csv")
    to_learn_dict = original_data.to_dict(orient="records")
else:
    to_learn_dict = data_frame.to_dict(orient="records")

def generate_new_cards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(canvas_image, image=bg_image)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_cards)

def is_known():
    to_learn_dict.remove(current_card)
    data = pandas.DataFrame(to_learn_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_new_cards()

#Button Setup
right_image = PhotoImage(file="C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day31/flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, padx=50, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="C:/Users/DEBKBANE/Desktop/100-Days-Udemy-Py/Day31/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, padx=50, command=generate_new_cards)
wrong_button.grid(row=1, column=2)

generate_new_cards()

window.mainloop()

