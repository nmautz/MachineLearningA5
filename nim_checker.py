"""
Date: 10/4/2022
Author: Caleb Barker
Desc: this File will run 4 tests on students nim players in order to check that they are defining their 
class and play function correctly. This checker also does some basic testing to make sure they are following the rules.  

Revision
Date: 09/28/23
Authon: Nathan Mautz
Desc: Added looped tests to make sure they are following the rules, and to find edge cases.
"""

import copy
import random
import traceback
import time
import sys



try:
    import nim_player 
    print("Test 1: Pass")
except:
    print("Test 1: Fail (Put this file in the same directory as your \'nim_player.py\'",end="")
    print(" Or, rename your file for the assignment to \'nim_player.py\')")

try:
    p1 = nim_player.NimPlayer()
    print("Test 2: Pass")
except:
    print("Test 3: Fail (Make sure that your class is named \'NimPlayer\')")    

try:
    p1.play([1,2,3,4])
    print("Test 3: Pass ")
except :
    print("Test 3: Fail (play should be defined as \"def play(self,board)\"")




def check():
    # updated to add random board - NM
    board = []
    board_length = 4
    for j in range(board_length):
        board.append(random.randint(0,8))
    start_board = board.copy()
    if board == [0,0,0,0]:
        return True,None
    #------
    while sum(board) != 1:
        prev_board = copy.deepcopy(board)
        board = p1.play(board)
        changes =0
        for i,val in enumerate(board):
            if val <0:
                print("Test 4: Fail (Returning negative number of sticks in board)")
                return False,start_board
            if val != prev_board[i]:
                changes +=1
            if val > prev_board[i]:
                print("Test 4: Fail (Increasing number of sticks in Board)")
                return False,start_board
        if changes > 1:
            print("Test 4: Fail (Changing multiple rows)") 
            return False,start_board
        if changes < 1:
            print("Test 4: Fail (No change to board state)")
            return False,start_board
    

    return True, None

#Checks many boards to check for edge cases - NM
try:
    def seconds_to_formatted_time(seconds):
        return str(int(seconds/60)) + " minutes " + str(int(seconds%60)) + " seconds"

    target = 1000000
    failed = 0
    passed = 0
    print("Test 4: Testing ", target, " boards")
    time_elapsed_s = 0

    for i in range(target):
        s_time = time.time()
        result,board = check()
        e_time = time.time()
        time_elapsed_s += e_time - s_time
        estimated_time_remaining_s = time_elapsed_s * (target - i) / (i + 1)
        if result:
            passed +=1
            if i%2000 == 0:
                sys.stdout.write("\rTest 4: Tested " + str(i) + " boards. " + seconds_to_formatted_time(estimated_time_remaining_s) + " seconds remaining")
                sys.stdout.flush()
        else:
            print()
            failed +=1
            print("Failed board: ", board)

        
    print()
    print("Passed: ", passed, " Failed: ", failed)
    if failed > 0:
        print("Test 4: Fail")
    else:
        print("Test 4: Pass")

except Exception as e:
    print("Test 4: Exception/Fail")
    traceback.print_exc() #Shows full exception - NM