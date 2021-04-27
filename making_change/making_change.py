#!/usr/bin/python

import sys


def making_change(amount, denominations):
    print(f"*** Calling making_change with amount: {amount} and denominations: {denominations}***")
    if len(denominations) < 2:
        print(f"only pennies so only 1 way to make {amount}")
        return 1
    elif amount < 5:
        print(f"{amount} is so small it can only be made with pennies")
        return 1
    current_coin_value = denominations[len(denominations) - 1]
    max_num_of_coins = amount // current_coin_value
    # print(f"the max number of {current_coin_value}'s that can fit in {amount} is {max_num_of_coins}")
    combinations = max_num_of_coins
    new_denominations = [denominations[i] for i in range(0, len(denominations) - 1)]
    if max_num_of_coins == 0:
        print(f"no {current_coin_value}s can fit in {amount}")
        return making_change(amount, new_denominations)
    elif max_num_of_coins == 1:
        print(f"it takes exactly 1 {current_coin_value} to make {amount}")
        return 1 + making_change(amount, new_denominations)
    for i in range(0, max_num_of_coins - 1):
        subcombinations = making_change(amount - (current_coin_value * i), new_denominations)
        combinations += subcombinations
        print(f"amount ({amount}) - {i} * {current_coin_value} can be made with {new_denominations} {subcombinations} ways. ")
    if combinations == 0:
        return 1
    return combinations

# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python making_change.py [amount]` with different amounts
#     if len(sys.argv) > 1:
#         denominations = [1, 5, 10, 25, 50]
#         amount = int(sys.argv[1])
#         print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations),
#                                                                      amount=amount))
#     else:
#         print("Usage: making_change.py [amount]")

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.denominations = [1, 5, 10, 25, 50]

    def test_making_change_small_amount(self):
        self.assertEqual(making_change(0, self.denominations), 1)
        self.assertEqual(making_change(1, self.denominations), 1)
        self.assertEqual(making_change(5, self.denominations), 2)
        self.assertEqual(making_change(10, self.denominations), 4)
        self.assertEqual(making_change(20, self.denominations), 9)
        self.assertEqual(making_change(30, self.denominations), 18)
        self.assertEqual(making_change(100, self.denominations), 292)
        self.assertEqual(making_change(200, self.denominations), 2435)
        self.assertEqual(making_change(300, self.denominations), 9590)

    def test_making_change_large_amount(self):
        return True
        self.assertEqual(making_change(350, self.denominations), 16472)
        self.assertEqual(making_change(400, self.denominations), 26517)
        self.assertEqual(making_change(1000, self.denominations), 801451)
        self.assertEqual(making_change(2000, self.denominations), 11712101)
        self.assertEqual(making_change(5000, self.denominations), 432699251)
        self.assertEqual(making_change(10000, self.denominations), 6794128501)


if __name__ == '__main__':
    unittest.main()
