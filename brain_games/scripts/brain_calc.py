from brain_games.games.logic_brain_calc import calc_round, CALC_RULES
from brain_games.games.games_logic import play_game


def main():
    play_game(calc_round, CALC_RULES)


if __name__ == '__main__':
    main()
