from data import QUESTION_DATA
from question_model import QuizGame


def main():
    """Main function"""
    quiz_game = QuizGame(QUESTION_DATA)

    while quiz_game.has_questions():
        question = quiz_game.get_next_question()
        answer = input(
            f"Q.{quiz_game.current_question_index}: {question['text']} (True/False): ").lower()
        if answer in ("true", "false", "t", "f"):
            quiz_game.check_answer(question, answer)
        else:
            print("Invalid input. Please enter 'True', 'False', 'T', or 'F'.")

    print(
        f"You've completed the quiz. Your final score is {quiz_game.score}/{quiz_game.current_question_index}")


if __name__ == "__main__":
    main()
