import random

from brain_games.games.games_logic import ask_question, play_game, get_random_number


def calculate_result(number_one: int, number_two: int, operation: str) -> int:
    if operation == '+':
        return number_one + number_two
    elif operation == '-':
        return number_one - number_two
    elif operation == '*':
        return number_one * number_two


def calc_round(username: str) -> bool:
    number_one = get_random_number()
    number_two = get_random_number()
    operation = random.choice(['+', '-', '*'])
    question = f'{number_one} {operation} {number_two}'
    correct_answer = str(calculate_result(number_one, number_two, operation))
    return ask_question(question, correct_answer, username)
