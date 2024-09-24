from brain_games.const import PROGRESSION_RULES
from brain_games.games.engine import play_game
from brain_games.games.progression import progression_round


def main():
    play_game(progression_round, PROGRESSION_RULES)


if __name__ == "__main__":
    main()
