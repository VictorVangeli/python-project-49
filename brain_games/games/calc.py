import random

from brain_games.const import CALC_RULES
from brain_games.games.engine import play_game
from brain_games.utils import get_random_number


def get_calculation__result(number_one: int, number_two: int, operation: str) -> int:
    """
    Вычисляет результат математической операции между двумя числами.

    Args:
        number_one (int): Первое число.
        number_two (int): Второе число.
        operation (str): Операция, которую нужно выполнить ('+', '-', '*').

    Returns:
        int: Результат выполнения операции.
    """
    match operation:
        case "+":
            return number_one + number_two
        case "-":
            return number_one - number_two
        case "*":
            return number_one * number_two


def get_numbers_and_calculation_result() -> tuple[str, str]:
    """
    Игроку задается случайное арифметическое выражение, и он должен ввести
    правильный ответ.
    Если ответ верный, раунд засчитывается как выигранный.


    Returns:
        tuple[str, str]: Кортеж, содержащий вопрос в виде строки и правильный
                         ответ в виде строки.
    """
    number_one, number_two = get_random_number(), get_random_number()
    operation = random.choice(["+", "-", "*"])
    question = f"{number_one} {operation} {number_two}"
    correct_answer = str(
        get_calculation__result(number_one, number_two, operation))
    return question, correct_answer


def run_calc_game():
    play_game(get_numbers_and_calculation_result, CALC_RULES)
