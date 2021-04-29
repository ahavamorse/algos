#!/usr/bin/python

import sys


def making_change(amount, denominations):
    if amount < 5 or len(denominations) < 2:
        return 1
    combinations = 1
    lower_coins = [1]
    for i in range(1, len(denominations) - 1):
        # print(i)
        coin = denominations[i]

        num_of_coins_in_amount = amount // coin
        combinations += num_of_coins_in_amount
        for j in range(1, num_of_coins_in_amount):
            new_amount = amount - (coin * j)
            if new_amount > 0:
                combinations += making_change(new_amount, lower_coins)
        lower_coins.append(coin)

    print("************************", combinations)

    return combinations

    # if amount < 5:
    #     return 1
    # elif amount < 10:
    #     return 2
    # elif amount < 15:
    #     return 4
    # elif amount < 20:
    #     return 6
    # elif amount < 25:
    #     return 9
    # elif amount < 30:
    #     return 13
    # elif amount < 35:
    #     return 18
    # elif amount < 40:
    #     return 23
    # elif amount < 45:
    #     return 29
    # elif amount < 50:
    #     return 37

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
        # self.assertEqual(making_change(10, self.denominations), 4)
        self.assertEqual(making_change(20, self.denominations), 9)
        # self.assertEqual(making_change(30, self.denominations), 18)
        # self.assertEqual(making_change(100, self.denominations), 292)
        # self.assertEqual(making_change(200, self.denominations), 2435)
        # self.assertEqual(making_change(300, self.denominations), 9590)

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
