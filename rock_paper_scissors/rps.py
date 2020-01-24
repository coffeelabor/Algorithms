#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  all_moves = []
  move_options = ['rock', 'paper', 'scissors']

  def helper_function(countdown, piece):
    if countdown == 0:
      all_moves.append(piece)
      return

    for move in move_options:    
      new_piece_result = piece + [move]
      helper_function(countdown - 1, new_piece_result)
  
  helper_function(n, [])
  return all_moves
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


'''
You'll want to define a list with all of the possible Rock Paper Scissors plays

i need to loop through my options array and add each option together until I get to n = 0

I need to have the 'count' be reduced by 1 each run of the fn

'''

'''
options = ['rock', 'paper', 'scissors']
  if n == 0:
    return [[]]
  elif n == 1:
    return [options]
  else:
    return options


'''


'''
def rock_paper_scissors(n):
  all_moves = []
  move_options = ['rock', 'paper', 'scissors']

  #Helper function(countdown for times left, peice of moves I am building up)
  def helper_function(countdown, piece):
    # If the counter is 0:
    if countdown == 0:
      #Attach the piece of moves to the all_moves
      all_moves.append(piece)
      return

    # for loop, for move in move_options
    for move in move_options:
      #variable = Add move to the end of piece of moves(scissors to the end of [paper, scissors,scissors])
      new_piece_result = piece + [move]
      #Call the Helper function(countdown - 1, variable)
      helper_function(countdown - 1, new_piece_result)
  
  #call the helper function with(number_of_plays, [])
  helper_function(n, [])
  # print('all_moves', all_moves)
  return all_moves

'''
