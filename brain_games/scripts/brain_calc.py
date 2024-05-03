#!/usr/bin/env python3
from brain_games.engine import game
from brain_games.games.calc import calc
from brain_games.games.calc import rules


def main():
    game(calc,rules)


if __name__ == '__main__':
    main()