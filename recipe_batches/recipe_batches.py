#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    plan_dict = {}
    amount = []
    for rk,  rv in recipe.items():
        print(f'keys values recipe {rk, rv}')
        for jk, jv in ingredients.items():
            print(f'keys values ingredients: {jk, jv}')

            # if jk = rk:
            #     temp = rv // jv
            #     amount.append({rk: temp})
            #     print(f'temp: {temp}')
            # elif jk != rk:
            #     plan_dict.update(rk: 0)
            #     print(f'test if')

            # if jk != rk:
            #     plan_dict.update(rk: 0)
            #     print(f'test if')
            # else:
            #     temp = rv // jv
            #     amount.append
            #     print(f'test else')

    print(f'final amount: {amount}')
    return amount


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


'''
understand

- im going to get two dictionaries
- the first dict is going to be a recipie that will have keys be the sting names and amount need to complete the recipie
-the second dict will have the keys be the string names of ingredients that I have available and the amounts I have available.  
- the problem wants me to first make sure that I have all the string ingredients (make sure that the keys match up 1:1)
-the problem also wants me to see if I have at a minimum the amount (values) for the recipie. 
- the problem also wants to see how many of the recipe I can do


plan
-Im going to need a variable for the amount that can be made.  probably should be an array so I can sort
-Im going to need to loop through the rk and rv for the recipe dict
  -Im going to need to do a jk and jv loop through the ingredients dict
    -first I should do an if to check if the key matches
      if its a match I can divide the rv by the jv and set that to the amount var
    -else if I hit a key in recipe that does not match anything in ingredients
      -return amount = 0
-I can return the first item in the array and 
'''
