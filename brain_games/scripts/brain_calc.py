from brain_games.const import CALC_RULES
from brain_games.games.games_logic import play_game
from brain_games.games.logic_brain_calc import calc_round


def main():
    play_game(calc_round, CALC_RULES)


if __name__ == "__main__":
    main()
