import math

from brain_games.const import GCD_RULES
from brain_games.games.engine import play_game
from brain_games.utils import get_random_number


def find_gcd(a: int, b: int) -> int:
    """
    Calculates the largest common divisor of two numbers

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: The largest common divisor of two numbers
    """
    return math.gcd(a, b)


def get_number_and_gcd_status() -> tuple[str, str]:
    """
    Conducts one round of the game to find the largest common divisor of two
    random numbers

    The player is asked to find the largest common divisor of two random numbers
    that are not equal to 1, and the smallest common divisor of which is not
    equal to 1

     If the player answers correctly, the game continues, if not, the game ends


    Returns:
        tuple[str, str]: A tuple containing a question as a string and the
        correct answer as a string
    """
    number_one, number_two = get_random_number(), get_random_number()
    question = f"{number_one} {number_two}"
    correct_answer = str(find_gcd(number_one, number_two))
    return question, correct_answer


def run_gcd_game():
    play_game(get_number_and_gcd_status, GCD_RULES)
