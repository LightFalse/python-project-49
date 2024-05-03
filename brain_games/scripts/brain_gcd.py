from brain_games.engine import game
from brain_games.games.gcd import gcd
from brain_games.games.gcd import rules


def main():
    game(gcd, rules)


if __name__ == "__main__":
    main()
