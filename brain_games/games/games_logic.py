import random

from brain_games.const import ENTER_NAME, GREETING_MESSAGE, ROUNDS


def get_random_number(start=1, end=100) -> int:
    """Возвращает случайное число в диапазоне от start до end."""
    return random.randint(start, end)


def ask_question(question: str, correct_answer: str, username: str) -> bool:
    """
    Задает вопрос пользователю и проверяет его ответ.

    Args:
        question (str): Вопрос, который будет задан пользователю.
        correct_answer (str): Ожидаемый правильный ответ.
        username (str): Имя пользователя для персонализированных сообщений.

    Returns:
        bool: True, если ответ правильный, иначе False.
    """
    print(f"Question: {question}")
    answer = input("Your answer: ").strip().lower()

    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(
            f'"{answer}" is wrong answer ;(. '
            f'Correct answer was "{correct_answer}".'
        )
        print(f"Let's try again, {username}!")
        return False


def play_game(game_round, game_rules: str):
    """
    Логика игры, которая повторяет вопросы, пока пользователь не ответит
    правильно несколько раз подряд.

    Args:
        game_round (Callable): Функция, которая описывает один раунд игры.
        game_rules (str): Правила игры, которые будут выведены перед началом.
    """
    counter = 0
    print(GREETING_MESSAGE)
    username = input(ENTER_NAME)
    print(f"Hello, {username}!")
    print(game_rules)

    while counter < ROUNDS:
        if game_round(username):
            counter += 1
        else:
            break

    if counter == ROUNDS:
        print(f"Congratulations, {username}!")
