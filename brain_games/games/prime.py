from brain_games.const import PRIME_RULES
from brain_games.games.engine import play_game
from brain_games.utils import get_random_number


def is_prime(number: int) -> bool:
    """
    Checks if the number is prime.
    If a number is divided by any number greater than its square root, then
    the other divisor will necessarily be less than the square root

    Args:
        number (int): An integer to check

    Returns:
        bool: True if number is prime, else False.
    """

    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_number_and_prime_status() -> tuple[str, str]:
    """
    Conducts one round of the game in which the player must guess whether the
    number is simple

    The player is given a random number and must answer 'yes' if the number
    simple, and 'no' if it is not simple. If the player answers correctly,
    the round is considered won


    Returns:
        tuple[str, str]: A tuple containing a question in the form of a string
        and the correct answer in the form of a string
    """
    number = get_random_number()
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def run_prime_game():
    play_game(get_number_and_prime_status, PRIME_RULES)
