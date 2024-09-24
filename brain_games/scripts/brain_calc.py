from brain_games.const import CALC_RULES
from brain_games.games.engine import play_game
from brain_games.games.calc import calc_round


def main():
    play_game(calc_round, CALC_RULES)


if __name__ == "__main__":
    main()
