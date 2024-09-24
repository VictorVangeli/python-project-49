from brain_games.games.engine import ask_question, get_random_number


def gcd(a: int, b: int) -> int:
    """
    Вычисляет наибольший общий делитель двух чисел

    Args:
        a (int): Первое число.
        b (int): Второе число.

    Returns:
        int: наименьший общий делитель двух чисел.
    """
    while b != 0:
        a, b = b, a % b
    return a


def gcd_round(username: str) -> bool:
    """
    Проводит один раунд игры на нахождение НОД двух случайных чисел.

    Игроку предлагается найти наибольший общий делитель двух случайных чисел,
    которые не равны 1, и наименьший общий делитель которых не равен 1.

    Если игрок отвечает правильно, игра продолжается, если нет - игра
    завершается.

    Args:
        username (str): Имя пользователя

    Returns:
        bool: True, если игрок дал правильный ответ, False в случае ошибки.
    """
    number_one = number_two = 1
    while (
        number_one == 1 or number_two == 1 or gcd(number_one, number_two) == 1
    ):
        number_one = get_random_number()
        number_two = get_random_number()
    question = f"{number_one} {number_two}"
    correct_answer = str(gcd(number_one, number_two))
    return ask_question(question, correct_answer, username)
