from brain_games.const import EVEN_RULES
from brain_games.games.games_logic import play_game
from brain_games.games.logic_brain_even import even_round


def main():
    play_game(even_round, EVEN_RULES)


if __name__ == "__main__":
    main()
