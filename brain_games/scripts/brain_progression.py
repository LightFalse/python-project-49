from brain_games.engine import game
from brain_games.games.progression import progression
from brain_games.games.progression import rules


def main():
    game(progression, rules)


if __name__ == "__main__":
    main()
