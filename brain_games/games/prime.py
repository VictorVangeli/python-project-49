from brain_games.const import PRIME_RULES
from brain_games.games.engine import play_game
from brain_games.utils import get_random_number


def is_prime(number: int) -> bool:
    """
    Проверяет, является ли число простым.
    Если число делится на какое-либо число больше своего квадратного корня, то
    другой делитель обязательно будет меньше квадратного корня

    Args:
        number (int): Целое число для проверки.

    Returns:
        bool: True, если число простое, иначе False.
    """

    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_number_and_prime_status() -> tuple[str, str]:
    """
    Проводит один раунд игры, в котором игрок должен угадать, является ли число
    простым.

    Игроку задается случайное число, и он должен ответить 'yes', если число
    простое, и 'no', если не является простым. Если игрок отвечает правильно,
    раунд считается выигранным.

    Args:
        username (str): Имя пользователя

    Returns:
        bool: True, если игрок дал правильный ответ, False в случае ошибки.
    """
    number = get_random_number()
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


def run_prime_game():
    play_game(get_number_and_prime_status, PRIME_RULES)
