from brain_games.const import EVEN_RULES
from brain_games.engine import play_game
from brain_games.utils import get_random_number


def is_even(number: int) -> bool:
    """
    Checks if the number is even

    Args:
        number (int): An integer to check

    Returns:
        bool: True if the number is even, otherwise False
    """
    return number % 2 == 0


def get_number_and_even_status() -> tuple[str, str]:
    """
    Conducts one round of the game in which the player must guess whether the
    number is even

     The player is given a random number, and he must answer 'yes' if the number
    is even, and 'no' if it is odd. If the player answers correctly, the round
    is considered won


    Returns:
        tuple[str, str]: A tuple containing a question as a string and the
        correct answer as a string
    """
    number = get_random_number()
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer


def run_even_game():
    play_game(get_number_and_even_status, EVEN_RULES)
