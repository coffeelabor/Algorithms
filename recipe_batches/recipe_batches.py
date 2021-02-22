#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  print('recipe', recipe)
  print('ingredients', ingredients)
  amount = []
  if len(recipe)>len(ingredients):
    return 0
  for rec_keys, rec_values in recipe.items():
    # print('rec_keys', rec_keys)
    # print('rec_values', rec_values)
    for ing_keys, ing_values in ingredients.items():
      # if len(rec_keys) > len(ing_keys):
      #   print('ok')
      if rec_keys == ing_keys:
        # amount.append(rec_values / ing_values)
        # amount.append(ing_values % rec_values)
        amount.append(math.floor(ing_values / rec_values))
      # elif rec_keys not in ing_keys:
      #   amount.append(0)
  amount.sort()
  print('amount', amount)
  return amount[0]

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


'''
I think I need to have a loop that matches up each of the keys in the dict

then I can do a mod between the recipe and ingredients and put them in an array

then I can sort the array and find return the smallest number

'''
