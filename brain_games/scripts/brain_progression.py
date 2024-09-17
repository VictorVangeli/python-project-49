from brain_games.games.games_logic import play_game
from brain_games.games.logic_brain_progression import progression_rules, progression_round


def main():
    play_game(progression_round, progression_rules)


if __name__ == '__main__':
    main()
