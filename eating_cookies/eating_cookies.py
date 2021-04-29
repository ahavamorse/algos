#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        cache[n] = 1
        return 1
    if n == 2:
        cache[n] = 2
        return 2
    if n == 3:
        cache[3] = 4
        return 4
    else:
        possibilities = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        cache[n] = possibilities
        return possibilities


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
#                                                                                     n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')

import unittest

class Test(unittest.TestCase):

  def test_eating_cookies_small_n(self):
    self.assertEqual(eating_cookies(0), 1)
    self.assertEqual(eating_cookies(1), 1)
    self.assertEqual(eating_cookies(2), 2)
    self.assertEqual(eating_cookies(5), 13)
    self.assertEqual(eating_cookies(10), 274)

  def test_eating_cookies_large_n(self):
    self.assertEqual(eating_cookies(50), 10562230626642)
    self.assertEqual(eating_cookies(100), 180396380815100901214157639)
    self.assertEqual(eating_cookies(500), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)


if __name__ == '__main__':
  unittest.main()
