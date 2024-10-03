from random import randint


def get_random_number(start=1, end=100) -> int:
    """Возвращает случайное число в диапазоне от start до end.

    Args:
        start (int): Начало диапазона случайный чисел
        end (int): Конец диапазона случайных чисел

    Returns:
        int: Случайное число
    """
    return randint(start, end)
