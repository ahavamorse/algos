#!/usr/bin/python

import sys


def add_possibilities(list_of_possibilities):
    new_list = []
    for possibility in list_of_possibilities:
        possibility.append("rock")
        new_list.append(possibility)
        possibility.pop()
        possibility.append("paper")
        new_list.append(possibility)
        possibility.pop()
        possibility.append("scissors")
        new_list.append(possibility)
    return new_list


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [["rock"], ["paper"], ["scissors"]]
    return add_possibilities(rock_paper_scissors(n - 1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

