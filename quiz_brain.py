class QuizBrain:
    def __init__(self, Qbank):
        self.question_number = 0
        self.question_list = Qbank
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        user_answer = input(
            f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}(True/False)?: ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
        print(f"Your current score is {self.score}/{self.question_number}.\n")

    def check_answer(self, user_answer, actual_answer):
        if user_answer == actual_answer:
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Correct answer is '{actual_answer}'")
