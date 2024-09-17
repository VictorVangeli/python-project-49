from brain_games.games.games_logic import play_game
from brain_games.games.logic_brain_gcd import gcd_round, GCD_RULES


def main():
    play_game(gcd_round, GCD_RULES)


if __name__ == '__main__':
    main()
