from random import shuffle


class QuizGame:
    """A class representing a quiz game."""

    def __init__(self, question_data):
        self.question_data = question_data.copy()
        shuffle(self.question_data)
        self.score = 0
        self.current_question_index = 0

    def has_questions(self):
        """Check if there are more questions to ask."""
        return self.current_question_index < len(self.question_data)

    def get_next_question(self):
        """Retrieve the next question."""
        question = self.question_data[self.current_question_index]
        self.current_question_index += 1
        return question

    def check_answer(self, question, answer):
        """Check the user's answer and update the score."""
        correct_answer = question["answer"].lower()
        if answer in ("true", "t") and correct_answer == "true" or \
           answer in ("false", "f") and correct_answer == "false":
            self.score += 1
            print(
                f"You got it right! \n The correct answer was: {question['answer']}. \n Your current score is: {self.score}/{self.current_question_index}")
        else:
            print(
                f"That's wrong. \n The correct answer was: {question['answer']}. \n Your current score is: {self.score}/{self.current_question_index}")
