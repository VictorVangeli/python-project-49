from brain_games.const import PRIME_RULES
from brain_games.games.games_logic import play_game
from brain_games.games.logic_brain_prime import prime_round


def main():
    play_game(prime_round, PRIME_RULES)


if __name__ == "__main__":
    main()
