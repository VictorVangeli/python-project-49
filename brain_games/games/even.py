from brain_games.const import EVEN_RULES
from brain_games.games.engine import ask_question, play_game
from brain_games.utils import get_random_number


def start_even_game():
    play_game(run_even_round, EVEN_RULES)


def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    Args:
        number (int): Целое число для проверки.

    Returns:
        bool: True, если число четное, иначе False.
    """
    return number % 2 == 0


def run_even_round(username: str) -> bool:
    """
    Проводит один раунд игры, в котором игрок должен угадать, является ли число
    четным.

    Игроку задается случайное число, и он должен ответить 'yes', если число
    четное, и 'no', если нечетное. Если игрок отвечает правильно, раунд
    считается выигранным.

    Args:
        username (str): Имя пользователя

    Returns:
        bool: True, если игрок дал правильный ответ, False в случае ошибки.
    """
    number = get_random_number()
    correct_answer = "yes" if is_even(number) else "no"
    return ask_question(f"{number}", correct_answer, username)
