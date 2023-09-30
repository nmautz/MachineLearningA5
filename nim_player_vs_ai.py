import copy
import random
import traceback
import time
import sys
import numpy as np
import random



try:
    import nim_player1
    print("Loaded nim_player1.py")
except:
    print("Couldn't find nim_player1.py")
  
try:
    import nim_player2
    print("Loaded nim_player2.py")
except:
    print("Couldn't find nim_player2.py")

def print_help():
    print("-------------------------------------------------")
    print("Usage: python nim_player_vs_ai.py [1|2] [1,1,1,1]")
    print("-------------------------------------------------")


np = nim_player1.NimPlayer()
try:
    if sys.argv[1] == '1':
        np = nim_player1.NimPlayer()
    elif sys.argv[1] == '2':
        np = nim_player2.NimPlayer()
    else: 
      print_help()

      print("Invalid argument, using default '1'")
except:
    print_help()
    
    print("Using default '1'")

board = []
try:
    board_str = sys.argv[2]
    board = [int(x) for x in board_str.split(",")]
    print("Using board: ", board)
except:
    board = [1,3,5,7]
    print_help()
    print("Using default board: ", board)


def is_board_lost(board):
    for i in range(len(board)):
        if board[i] > 0:
            return False
    return True

winner = None
player_first_move = random.randint(0,1)
if player_first_move == 0:
    print("Player goes first")
else:
    print("AI goes first")

def is_valid_move(board, new_board):
  columns_changed = 0
  
  for i in range(len(board)):
      if board[i] != new_board[i]:
          columns_changed += 1
          if board[i] < new_board[i]:
              return False
          if board[i] < 0:
              return False
  return columns_changed == 1    

def player_play(board):

    stupid_bool = False
    new_board = [-1,-1,-1,-1]
    print(board)
    print("---------")
    while not is_valid_move(board, new_board):
      if stupid_bool:
        print("Invalid move, try again")
      else:
        stupid_bool = True

      print("Enter new board state")
      print("---------")
      new_board_str = input()
      new_board = [int(x) for x in new_board_str.split(",")]


while winner == None:
    print(board)
    if player_first_move == 0:
        print("Player's turn")
        #TODO
    else:
        print("AI's turn")
        board = np.play(board)
        print(board)
        