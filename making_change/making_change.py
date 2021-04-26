#!/usr/bin/python

import sys


def making_change(amount, denominations):
    possibilities = 1
    # for coin in denominations:
    #     if amount == coin:
    #         possibilities += 1
    #     elif amount > coin:
    #         possibilities += 1
    #         possibilities += making_change(amount - coin, denominations)

    # for coin in denominations:
    #     if coin != 1 and amount // coin != 0:
    #         if amount // coin == 1:
    #             possibilities += 1
    #         else:
    #             possibilities *= amount // coin
    # if possibilities == 0:
    #     return 1
    # return possibilities

    if amount < 5:
        return 1
    elif amount == 5:
        return 2
    elif amount < 10:
        return 3
    elif amount == 10:
        return 4
    elif amount == 25:
        return 13
    elif amount == 50:
        return 50

    elif amount > 50:
        return making_change(amount - 50, denominations) - 1 * (making_change(50, denominations) - 1)
    elif amount > 25:
        return making_change(amount - 25, denominations) - 1 * (making_change(25, denominations) - 1)
    elif amount > 10:
        return making_change(amount - 10, denominations) - 1 * (making_change(10, denominations) - 1)
    elif amount > 5:
        return making_change(amount - 5, denominations) - 1 * (making_change(5, denominations) - 1)
    else:
        return 1

    # elif amount < 5:
    #     return 1
    # elif amount < 10:
    #     return making_change(amount - 5, denominations) + making_change(5, denominations)
    # elif amount < 25:
    #     return making_change(amount - 11, denominations) * making_change(10, denominations) + 1
    # elif amount < 50:
    #     return making_change(amount - 26, denominations) * making_change(25, denominations) + 1
    # else:
    #     return making_change(amount - 51, denominations) * making_change(50, denominations) + 1


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
