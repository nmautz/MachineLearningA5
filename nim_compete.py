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

    target = 10000
    failed = 0
    passed = 0
    print("Testing ", target, " boards")
    time_elapsed_s = 0

    for i in range(target):
        s_time = time.time()

        

        e_time = time.time()
        time_elapsed_s += e_time - s_time
        estimated_time_remaining_s = time_elapsed_s * (target - i) / (i + 1)
        if i%2000 == 0:
          sys.stdout.write("\rTest 4: Tested " + str(i) + " boards. " + seconds_to_formatted_time(estimated_time_remaining_s) + " seconds remaining")
          sys.stdout.flush()


        
    print()
    print("Passed: ", passed, " Failed: ", failed)
    if failed > 0:
        print("Test 4: Fail")
    else:
        print("Test 4: Pass")

except Exception as e:
    print("Test 4: Exception/Fail")
    traceback.print_exc() #Shows full exception - NM