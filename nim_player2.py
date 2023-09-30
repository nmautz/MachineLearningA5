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

  def get_state_score(self,state_arr, is_friendly_turn):
    if state_arr == [0,0,0,0] and is_friendly_turn:
      return -1
    elif state_arr == [0,0,0,0] and not is_friendly_turn:
      return 1
    else:
      next_states = self.get_next_states(state_arr)
      score = 0
      for next_state in next_states:
        score += self.get_state_score(next_state, not is_friendly_turn)
      return score

  def play(self, state_arr):
    next_states = self.get_next_states(state_arr)
    if len(next_states) == 0:
      print(state_arr)
      return state_arr
    best_state = next_states[0]
    best_score = self.get_state_score(best_state, False)
    for next_state in next_states:
      score = self.get_state_score(next_state, False)
      if score > best_score:
        best_state = next_state
        best_score = score
    return best_state
      
    