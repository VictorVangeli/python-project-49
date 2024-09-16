from brain_games.games.games_logic import get_random_number, ask_question, play_game


def is_even(number: int) -> bool:
    return number % 2 == 0


def even_round(username: str) -> bool:
    number = get_random_number()
    correct_answer = 'yes' if is_even(number) else 'no'
    return ask_question(f'{number}', correct_answer, username)


def main():
    play_game(even_round)
