from brain_games.const import EVEN_RULES
from brain_games.games.engine import play_game
from brain_games.utils import get_random_number


def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    Args:
        number (int): Целое число для проверки.

    Returns:
        bool: True, если число четное, иначе False.
    """
    return number % 2 == 0


def get_number_and_even_status() -> tuple[str, str]:
    """
    Проводит один раунд игры, в котором игрок должен угадать, является ли число
    четным.

    Игроку задается случайное число, и он должен ответить 'yes', если число
    четное, и 'no', если нечетное. Если игрок отвечает правильно, раунд
    считается выигранным.


    Returns:
        tuple[str, str]: Кортеж, содержащий вопрос в виде строки и правильный
                         ответ в виде строки.
    """
    number = get_random_number()
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer


def run_even_game():
    play_game(get_number_and_even_status, EVEN_RULES)
