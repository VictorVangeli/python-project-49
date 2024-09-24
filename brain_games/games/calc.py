import random

from brain_games.games.engine import ask_question, get_random_number


def calculate_result(number_one: int, number_two: int, operation: str) -> int:
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


def calc_round(username: str) -> bool:
    """
    Игроку задается случайное арифметическое выражение, и он должен ввести
    правильный ответ.
    Если ответ верный, раунд засчитывается как выигранный.

    Args:
        username (str): Имя пользователя

    Returns:
        bool: True, если игрок дал правильный ответ, False в случае ошибки.
    """
    number_one, number_two = get_random_number(), get_random_number()
    operation = random.choice(["+", "-", "*"])
    question = f"{number_one} {operation} {number_two}"
    correct_answer = str(calculate_result(number_one, number_two, operation))
    return ask_question(question, correct_answer, username)
