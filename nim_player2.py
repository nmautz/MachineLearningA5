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
 
  def get_state_score_h(self, state_arr, depth, is_friendly_turn):

    if np.array_equal(state_arr, [0,0,0,0]):
      if is_friendly_turn: #friendly wins this scenario
        return 1
      else: #friendly loses this scenario
        return -1

    if depth != 0:
      next_states = self.get_next_states(state_arr)
      score = 0
      for next_state in next_states:
        nim_sum_next_state = self.nim_sum(next_state)
        if nim_sum_next_state != 0 and is_friendly_turn or nim_sum_next_state == 0 and not is_friendly_turn:
          score += self.get_state_score_h(next_state, depth-1, not is_friendly_turn)
      return score / len(next_states)
    else:
      if self.nim_sum(state_arr) == 0:
        if is_friendly_turn: #winning state
          return 0.25
        else: #losing state
          return -0.25
      else:
        if is_friendly_turn: #losing state
          return -0.25
        else: #winning state
          return 0.25

    

  def get_state_score(self, state_arr, depth):
    return self.get_state_score_h(state_arr, depth, True)
    
  def play(self, state_arr):
    next_states = self.get_next_states(state_arr)
    if len(next_states) == 0:
      return [0,0,0,0]
    
    best_score = None
    best_state = None

    for next_state in next_states:
      score = self.get_state_score(next_state, 2)
      if best_score == None or score > best_score:
        best_score = score
        best_state = next_state

    
    return best_state
  
      
      
