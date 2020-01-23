#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # pass
  small_price = {}
  for price in range(0, len(prices)):
    small_price[price] = prices[price]
  print('small price', small_price)
  for key, value in small_price:
    
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



'''
there needs to be a variable for the largest number
there needs to be a variable for the smallest number
I need to make sure the smallest number is first and the largest comes after 





'''
