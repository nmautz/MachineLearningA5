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


#Checks many boards
try:
    def seconds_to_formatted_time(seconds):
        return str(int(seconds/60)) + " minutes " + str(int(seconds%60)) + " seconds"
    target = 100
    try:
      target = int(sys.argv[1])
    except:
      print("Error: ./nim_complete (runcount).... continuing with default value 100")
      time.sleep(2)
    p1_wins = 0
    p2_wins = 0
    np1_wins = 0
    np2_wins = 0
    print("Testing ", target, " boards")
    print()
    time_elapsed_s = 0
    def is_board_lost(board):
        return board == [0,0,0,0]

    for i in range(target):
        s_time = time.time()

        board = []
        board_length = 4
        for j in range(board_length):
          board.append(random.randint(1,8))
          
        does_player_one_starts_first = bool(random.randint(0,1))
        p1 = nim_player1.NimPlayer()
        p2 = nim_player2.NimPlayer()
        player_1 = 1
        if does_player_one_starts_first == 0:
          p1 = nim_player2.NimPlayer()
          p2 = nim_player1.NimPlayer()
          player_1 = 2

        p1_winner = None
        while p1_winner == None:
            board = p1.play(board)
            if is_board_lost(board):
              p1_winner = False
            else:
              board = p2.play(board)
              if is_board_lost(board):
                p1_winner = True

        if p1_winner:
            p1_wins += 1
            if player_1 == 1:
                np1_wins += 1
            else:
                np2_wins += 1
        else:
            p2_wins += 1  
            if player_1 == 1:
                np2_wins += 1
            else:
                np1_wins += 1
        
        e_time = time.time()
        time_elapsed_s += e_time - s_time
        estimated_time_remaining_s = time_elapsed_s * (target - i) / (i + 1)
        sys.stdout.write("\rTested " + str(i) + " boards. " + seconds_to_formatted_time(estimated_time_remaining_s) + " seconds remaining")
        sys.stdout.flush()


        
    print()
    print("P1 Wins: ", p1_wins, " p2 Wins: ", p2_wins)
    print("P1 Win/Loss Ratio:", p1_wins/target, " P2 Win/Loss Ratio:", p2_wins/target)

    print("Nim Player 1 Wins: ", np1_wins, " Nim Player 2 Wins: ", np2_wins)
    print("Nim Player 1 Win/Loss Ratio:", np1_wins/target, " Nim Player 2 Win/Loss Ratio:", np2_wins/target)
  

except Exception as e:
    print("Test 4: Exception/Fail")
    traceback.print_exc() #Shows full exception - NM