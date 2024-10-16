import random

from brain_games.const import CALC_RULES
from brain_games.engine import play_game
from brain_games.utils import get_random_number


def get_random_math_sign_and_result(number_one: int, number_two: int) -> dict:
    """
    Calculates the result of a mathematical operation between two numbers and
    returns the operation and the result in the form of a dictionary.

    Args:
        number_one (int): The first number
        number_two (int): The second number

    Returns:
        dict: A dictionary with the mathematical sign as the key and the result
              of the operation as the value.
    """
    return {
        "+": number_one + number_two,
        "-": number_one - number_two,
        "*": number_one * number_two,
    }


def get_numbers_and_calculation_result() -> tuple[str, str]:
    """
    The player is given a random arithmetic expression and must enter
    the correct answer.
    If the answer is correct, the round is counted as won.

    Returns:
        tuple[str, str]: A tuple containing a question in the form of a string
        and the correct answer in the form of a string.
    """
    number_one, number_two = get_random_number(), get_random_number()
    operations_dict = get_random_math_sign_and_result(number_one, number_two)

    operation = random.choice(list(operations_dict.keys()))

    question = f"{number_one} {operation} {number_two}"
    correct_answer = str(operations_dict[operation])

    return question, correct_answer


def run_calc_game():
    play_game(get_numbers_and_calculation_result, CALC_RULES)
