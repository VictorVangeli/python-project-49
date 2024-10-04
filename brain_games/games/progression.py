from brain_games.const import PROGRESSION_RULES
from brain_games.games.engine import play_game
from brain_games.utils import get_random_number


def get_progression_and_missed_number() -> tuple[str, str]:
    """
    Generates an arithmetic progression and hides one of its elements

    Returns:
        tuple[str, str]: A tuple containing a question as a string and the
        correct answer as a string
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

    return question, correct_answer


def run_progression_game():
    play_game(get_progression_and_missed_number, PROGRESSION_RULES)
