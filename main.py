from data import question_data, answer_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
answer_bank = []

for i in range(0,10):

    question_text = question_data[i]
    answer_text = answer_data[i]
    question_bank.append(question_text)
    answer_bank.append(answer_text)

quiz_ui = QuizInterface()

quiz = QuizBrain(question_bank)

#quiz_ui.update_ui()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
