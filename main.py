import random

class IQTest:
    def __init__(self):
        self.questions = [
            {"question": "What comes next in the sequence: 1, 4, 9, 16, ...?", "options": ["25", "36", "49", "64"], "answer": "64"},
            {"question": "If all Bloops are Razzies, and all Razzies are Lazzies, then all Bloops are definitely Lazzies. True or False?", "options": ["True", "False"], "answer": "True"},
            {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "Which of the following words is least like the others?", "options": ["Dog", "Cat", "Mouse", "Lion"], "answer": "Mouse"},
            # Add more questions here
        ]
        self.score = 0

    def start_test(self):
        print("Welcome to the IQ Test Simulator!")
        print("You will be presented with a series of questions. Choose the correct answer for each question.")
        print("Let's begin:\n")

        for i, question in enumerate(self.questions):
            print(f"Question {i+1}: {question['question']}")
            for j, option in enumerate(question['options']):
                print(f"{j+1}. {option}")

            user_answer = input("Your answer: ").strip().capitalize()
            if user_answer == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}")

            print()

        print(f"Test completed! Your IQ score is: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    test = IQTest()
    test.start_test()
