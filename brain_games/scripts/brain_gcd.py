from brain_games.const import GCD_RULES
from brain_games.games.engine import play_game
from brain_games.games.gcd import gcd_round


def main():
    play_game(gcd_round, GCD_RULES)


if __name__ == "__main__":
    main()
