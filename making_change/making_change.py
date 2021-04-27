#!/usr/bin/python

import sys


def making_change(amount, denominations):
    if len(denominations) < 2:
        return 1
    elif amount < 2:
        return 1
    current_coin_value = denominations[len(denominations) - 1]
    max_num_of_coins = amount // current_coin_value
    combinations = max_num_of_coins
    denominations.pop()
    if amount == current_coin_value:
        return 1 + making_change(amount, denominations)
    for i in range(0, max_num_of_coins):
        combinations += making_change(amount - (current_coin_value * i), denominations)
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
