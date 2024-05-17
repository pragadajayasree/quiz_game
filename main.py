from data import question_data
from question_model import  Question
from quiz_brain import QuizBrain
question_bank=[]

for i in question_data:
    text=i["text"]
    answer=i["answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
   quiz.next_question()

print("You have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")