class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
    def ask_question(self):
        user_response = input(f"Q.{self.question_number + 1} {self.list[self.question_number].question}(True/False): ").lower()
        return user_response
    def still_questions(self):
        if self.question_number < len(self.list):
            return True
        else:
            return False
    def next_question(self):
        self.question_number = self.question_number + 1
    def check_answer(self):
        if self.ask_question() == (self.list[self.question_number].answer).lower():
            print(f"That is correct, {self.list[self.question_number].question} is {self.list[self.question_number].answer}")
            return True
        else:
            print(f"That is wrong,{self.list[self.question_number].question} is {self.list[self.question_number].answer} ")
            return False

