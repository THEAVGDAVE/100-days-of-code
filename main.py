from data import minecraft_questions
from  question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in minecraft_questions:
    just_questions = Question(question['question'], question['answer'])
    question_bank.append(just_questions)

questions = QuizBrain(question_bank)
still_playing = True
score = 0
total = 0
while still_playing:
    if questions.still_questions():
        if questions.check_answer():
            score = score + 1
        questions.next_question()
        total = total + 1
        print(f"Your current score is {score}/{total}")
        print("\n" * 2)
    else:
        print(f"You got {score}/{total} ")
        still_playing = False
