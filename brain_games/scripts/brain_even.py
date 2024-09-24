from brain_games.const import EVEN_RULES
from brain_games.games.engine import play_game
from brain_games.games.even import even_round


def main():
    play_game(even_round, EVEN_RULES)


if __name__ == "__main__":
    main()
