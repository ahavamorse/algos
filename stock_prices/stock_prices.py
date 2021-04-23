#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # First attempt - naive approach
    # First find a low price to buy at
    lowest_price_index = 0
    for current_index in range(1, len(prices) - 1):
        if prices[current_index] < prices[lowest_price_index]:
            lowest_price_index = current_index

    # Next find a high price (that comes later) to sell at
    highest_following_price_index = 0
    for current_index in range(lowest_price_index, len(prices) - 1):
        if prices[current_index] > prices[highest_following_price_index]:
            highest_following_price_index = current_index

    # Find the difference of the prices to find the profit
    profit = prices[highest_following_price_index] - prices[lowest_price_index]
    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
