from brain_games.games.games_logic import play_game
from brain_games.games.logic_brain_prime import prime_round, prime_rules


def main():
    play_game(prime_round, prime_rules)


if __name__ == '__main__':
    main()
