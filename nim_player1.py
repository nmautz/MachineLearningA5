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
    if len(next_states) == 0 or [0,0,0,0] in next_states:
      return [0,0,0,0]
  
    for next_state in next_states:

      if self.nim_sum(next_state) == 0:
        return next_state
        
      
    return next_states[0]
