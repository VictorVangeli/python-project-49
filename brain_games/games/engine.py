from brain_games.const import ENTER_NAME, GREETING_MESSAGE, ROUNDS_NUMBERS


def play_game(game_round, game_rules: str):
    """
    The logic of the game, which repeats the questions until the user answers
    correctly several times in a row

    Args:
        game_round (Callable): A function that describes one round of the game.
        game_rules (str): The rules of the game that will be displayed before
        the start
    """
    print(GREETING_MESSAGE)
    username = input(ENTER_NAME)
    print(f"Hello, {username}!")
    print(game_rules)

    for _ in range(ROUNDS_NUMBERS):
        question, correct_answer = game_round()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip().lower()

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f'"{answer}" is wrong answer ;(. '
                f'Correct answer was "{correct_answer}".'
            )
            print(f"Let's try again, {username}!")
            return

    print(f"Congratulations, {username}!")
