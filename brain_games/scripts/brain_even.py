from brain_games.engine import game
from brain_games.games.even import even
from brain_games.games.even import rules


def main():
    game(even, rules)


if __name__ == "__main__":
    main()
