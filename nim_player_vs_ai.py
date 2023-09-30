import copy
import random
import traceback
import time
import sys
import numpy as np



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
