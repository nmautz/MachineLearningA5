import copy
import random
import traceback
import time
import sys
import numpy as np
import random



try:
    import nim_player1
except:
    print("Couldn't find nim_player1.py")
    exit()
  

board = sys.argv[1]
board = board.split(",")
board = [int(i) for i in board]
print(nim_player1.NimPlayer().play(board))
