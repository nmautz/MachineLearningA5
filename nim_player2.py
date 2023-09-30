#Nathan Mautz
#09/29/23
#Nim player that calculates all possible moves and plays the first one.
import numpy as np
class NimPlayer:
  
  def __init__(self):
    pass

  def is_game_won(self, state_arr):
    return len(self.get_next_states(state_arr)) == 0
    
  def nim_sum(self, state_arr):
    total = 0
    for number in state_arr:
      total ^= number
    return total

  def get_state_score(state_arr, depth):
    return 1

  def get_next_states(self, state_arr):
    next_states_arr = []  
    for number in state_arr:
      if number > 0:
        for i in range(1, number+1):
          new_state = state_arr.copy()
          new_state[state_arr.index(number)] -= i
          if not np.array_equal(new_state, state_arr):
            next_states_arr.append(new_state.copy())
    return next_states_arr

  def play(self, state_arr):
    next_states = self.get_next_states(state_arr)
    if len(next_states) == 0:
      return [0,0,0,0]
    
    best_score = None
    best_state = None

    for next_state in next_states:
      score = self.get_state_score(next_state, 4)
      if best_score == None or score < best_score:
        best_score = score
        best_state = next_state

    
    return best_state
  
      
      
