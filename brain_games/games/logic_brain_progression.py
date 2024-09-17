import random

from brain_games.games.games_logic import ask_question

PROGRESSION_RULES = 'What number is missing in the progression?'


def progression_round(username: str) -> bool:
    """
    Генерирует арифметическую прогрессию и скрывает один из ее элементов.

    Returns:
        tuple: Кортеж из строки с прогрессией (где один элемент заменен на '..') и правильного ответа.
    """
    start = random.randint(1, 100)
    step = random.randint(1, 40)
    length = random.randint(5, 10)

    progression_list = [start + step * i for i in range(length)]

    hide_elements = random.randint(0, len(progression_list) - 1)
    correct_answer = str(progression_list[hide_elements])
    progression_list[hide_elements] = '..'
    question = ' '.join(map(str, progression_list))

    return ask_question(question, correct_answer, username)
