import math

from brain_games.const import GCD_RULES
from brain_games.games.engine import play_game
from brain_games.utils import get_random_number


def start_gcd_game():
    play_game(run_gcd_round, GCD_RULES)


def find_gcd(a: int, b: int) -> int:
    """
    Вычисляет наибольший общий делитель двух чисел

    Args:
        a (int): Первое число.
        b (int): Второе число.

    Returns:
        int: Наибольший общий делитель двух чисел.
    """
    return math.gcd(a, b)


def run_gcd_round() -> tuple[str, str]:
    """
    Проводит один раунд игры на нахождение НОД двух случайных чисел.

    Игроку предлагается найти наибольший общий делитель двух случайных чисел,
    которые не равны 1, и наименьший общий делитель которых не равен 1.

    Если игрок отвечает правильно, игра продолжается, если нет - игра
    завершается.

    Args:
        username (str): Имя пользователя

    Returns:
        tuple[str, str]: Кортеж, содержащий вопрос в виде строки и правильный
                         ответ в виде строки.
    """
    number_one, number_two = get_random_number(), get_random_number()
    if (
        number_one == 1
        or number_two == 1
        or find_gcd(number_one, number_two) == 1
    ):
        return run_gcd_round()
    question = f"{number_one} {number_two}"
    correct_answer = str(find_gcd(number_one, number_two))
    return question, correct_answer
