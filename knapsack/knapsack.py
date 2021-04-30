#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

'''
from itertools import product

all_possiblities = list(product[1, 2, 3], repeat=3)
'''


def knapsack_solver(items, capacity):
    # Different ways to solve include...
    # naive: grab most valuable items until knapsack is full
    # brute strength: try every possible combination and find best one
    # greedy: rank according to efficiency (value / weight) and grab items until knapsack is full
    pass

def goldmine_solver():
    # Different ways to solve include...
    # brute force: try all combinations and compare
    # naive: choose best possible spot each time
    # greedy: work backward to know ahead of time which is the most valuable path
    pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
