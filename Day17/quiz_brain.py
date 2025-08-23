class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 1
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        print('WELCOME TO THE QUIZ GAME....... ')
        print('\n'*3)
        for item in self.question_list:
            user_choice = input(f"Q.{self.question_number} {item.text} (True/False)?\t").title()
            if(user_choice==item.answer):
                self.question_number += 1
                self.score += 1
            else:
                self.question_number += 1

        print(f"\nWe are at the end of the quiz, your final score is: {self.score}/12")
