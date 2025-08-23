from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_FONT = ("Arial", 20, "italic")

class QuizInterface():
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #Create the score label
        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        #Create the canvas for the questions to pop up
        self.canvas = Canvas(self.window, width=300, height=250, background="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Welcome to Quizler!",
            width=280,
            font=CANVAS_FONT,
            fill=THEME_COLOR)
        #Create the right and wrong button
        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        self.right = Button(text="", image=right_image, highlightthickness=0, command=self.is_right)
        self.right.grid(row=2, column=0)
        self.wrong = Button(text="", image=wrong_image, highlightthickness=0, command=self.is_wrong)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.current_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.current_question)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz, the score is reflected above")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def is_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

