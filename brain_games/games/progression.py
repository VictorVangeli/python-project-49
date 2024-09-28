from brain_games.const import PROGRESSION_RULES
from brain_games.games.engine import ask_question, play_game
from brain_games.utils import get_random_number


def get_progression_and_missed_number(username: str) -> bool:
    """
    Генерирует арифметическую прогрессию и скрывает один из ее элементов.

    Returns:
        tuple: Кортеж из строки с прогрессией (где один элемент заменен на '..')
         и правильного ответа.
    """
    start = get_random_number(1, 100)
    step = get_random_number(1, 40)
    length = get_random_number(5, 10)
    hide_index = get_random_number(0, length - 1)

    question = " ".join(
        ".." if i == hide_index else str(start + i * step)
        for i in range(length)
    )

    correct_answer = str(start + hide_index * step)

    return ask_question(question, correct_answer, username)


def run_progression_game():
    play_game(get_progression_and_missed_number, PROGRESSION_RULES)
