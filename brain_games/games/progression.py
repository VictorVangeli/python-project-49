from brain_games.const import PROGRESSION_RULES
from brain_games.games.engine import ask_question, play_game
from brain_games.utils import get_random_number


def start_progression_game():
    play_game(run_progression_round, PROGRESSION_RULES)


def run_progression_round(username: str) -> bool:
    """
    Генерирует арифметическую прогрессию и скрывает один из ее элементов.

    Returns:
        tuple: Кортеж из строки с прогрессией (где один элемент заменен на '..')
         и правильного ответа.
    """
    start = get_random_number(1, 100)
    step = get_random_number(1, 40)
    length = get_random_number(5, 10)

    progression_list = [start + step * i for i in range(length)]

    hide_index = get_random_number(0, length - 1)
    correct_answer = str(progression_list[hide_index])
    question = " ".join(
        ".." if i == hide_index else str(num)
        for i, num in enumerate(progression_list)
    )

    return ask_question(question, correct_answer, username)
