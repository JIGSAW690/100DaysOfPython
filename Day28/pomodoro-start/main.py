import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = ("Courier", 30, "bold")
TIMER_FONT = ("Courier", 40, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    checkbox_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_minutes = WORK_MIN * 60
    short_break_minutes = SHORT_BREAK_MIN * 60
    long_break_minutes = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_minutes)
        timer_label.config(text="Long BREAK...", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_minutes)
        timer_label.config(text="SHORT BREAK...", fg=RED)
    else:
        count_down(work_minutes)
        timer_label.config(text="WORK TIME...", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps / 2)
        marks = ""
        for _ in range(work_sessions):
            marks += "✓"
        checkbox_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(window, width=224, height=250, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",  font=FONT_NAME)

timer_label = Label(window, text="TIMER", font=TIMER_FONT, fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

checkbox_label = Label(window, text="", font=TIMER_FONT, fg=GREEN, bg=YELLOW, highlightthickness=0)
checkbox_label.grid(row=2, column=1)

start = Button(window, text="START", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(window, text="RESET", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()