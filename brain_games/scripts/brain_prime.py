from brain_games.engine import game
from brain_games.games.prime import prime
from brain_games.games.prime import rules


def main():
    game(prime, rules)


if __name__ == "__main__":
    main()