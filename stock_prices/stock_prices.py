#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # First attempt - naive approach
    # First find a low price to buy at
    # lowest_price_index = 0
    # for current_index in range(1, len(prices) - 1):
    #     if prices[current_index] < prices[lowest_price_index]:
    #         lowest_price_index = current_index
    #
    # # Next find a high price (that comes later) to sell at
    # highest_following_price_index = 0
    # for current_index in range(lowest_price_index, len(prices) - 1):
    #     if prices[current_index] > prices[highest_following_price_index]:
    #         highest_following_price_index = current_index
    #
    # # Find the difference of the prices to find the profit
    # profit = prices[highest_following_price_index] - prices[lowest_price_index]
    # return profit

    # Second attempt - Brute force
    # best_profit = 0
    # for i in range(0, len(prices) - 1):
    #     for j in range(i, len(prices) - 1):
    #         if prices[j] - prices[i] > best_profit:
    #             best_profit = prices[j] - prices[i]
    # if best_profit == 0:
    #     return -10
    # return best_profit

    # Third attempt - improved naive approach
    lowest_price_index = 0
    highest_price_index = 1
    profit = prices[highest_price_index] - prices[lowest_price_index]

    for i in range(1, len(prices) - 1):
        if prices[i] < prices[lowest_price_index]:
            lowest_price_index = i
        if prices[i] > prices[highest_price_index]:
            highest_price_index = i
    if highest_price_index > lowest_price_index:
        profit = prices[highest_price_index] - prices[lowest_price_index]
        return profit
    else:
        highest_price_index = lowest_price_index
        for i in range(lowest_price_index + 1, len(prices)):
            if prices[i] > prices[highest_price_index]:
                highest_price_index = i
    return profit



if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
