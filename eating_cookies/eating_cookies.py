#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # if cache is None:
  if cache is None or type(cache) == list:
    # cache = [1,1,2]
    cache = {0:1, 1:1, 2:2}
  if n < 0:
    return 0
  # elif cache[n] == 0:
  elif n not in cache:
    return eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache) 
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


'''
guess im gonna use recursion 

the result is the sum of the previous results in factorial order

its only the last three: n-3, n-2, n-1

'''

'''
GUIDED PT1

if cache is None:
    cache = {0: 1, 1:1, 2:2, 3:4}
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3) + eating_cookies(n-4) 

Part 2
if cache is None:
    cache = {0: 1, 1:1, 2:2}
  if n < 0:
    return 0
  elif n not in cache:
    return eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache) 
  return cache[n]


if cache is None:
    cache = {0: 1, 1:1, 2:2, 3:4}
  if n < 0:
    return 0
  elif n not in cache:
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3) + eating_cookies(n-4)
  return cache[n]

'''
