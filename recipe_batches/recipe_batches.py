#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batch = 100
    for key in recipe:
        if ingredients.keys().__contains__(key):
            if ingredients[key] // recipe[key] < max_batch:
                max_batch = ingredients[key] // recipe[key]
        else:
            max_batch = 0
    return max_batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
