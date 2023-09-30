#Nathan Mautz
#09/29/23
#Nim player that calculates all possible moves and plays the first one.
import numpy as np
class NimPlayer:
  
  def __init__(self):
    self.winning_states = [[0,0,2,2],[0,0,3,3], [0,0,4,4], [0,0,5,5], [0,0,6,6], [0,0,7,7], [0,0,8,8], [0,0,9,9], [0,1,1,1], [0,1,2,3], [0,1,4,5], [0,1,6,7], [0,1,8,9], [0,2,4,6], [0,2,5,7], [0,3,4,7], [0,3,5,6], [0,4,8,12], [0,4,9,13], [0,5,8,13], [0,5,9,12], [1,2,4,7],[1,2,5,6], [1,3,4,6],[1,3,5,7], [2,3,4,5], [2,3,8,9], [4,5,6,7], [4,5,8,9]]                                       

    for i in range (0,12):
      for j in range (0,12):
        self.winning_states.append([i,i,j,j])
      self.winning_states.append([i,i,i,i])



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
    for next_state in next_states:
      if not next_state in self.winning_states:
        return next_state
    
    if len(next_states) == 0:
      return [0,0,0,0]
      
    return next_states[0]
