from data import question_data, question_data1
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for data in question_data1:
    question_bank.append(Question(data["question"],data["correct_answer"]))

# for keys in question_bank:
#     print(keys.text+":"+keys.answer)
#
newQuiz = QuizBrain(question_bank)

while newQuiz.still_has_question():
    newQuiz.next_question()

print("You have completed the quiz")
print(f"Your final score is: {newQuiz.score}/{newQuiz.question_number}")
