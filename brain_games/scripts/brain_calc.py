from brain_games.games.logic_brain_calc import calc_round, calc_rules
from brain_games.games.games_logic import play_game


def main():
    play_game(calc_round, calc_rules)


if __name__ == '__main__':
    main()
