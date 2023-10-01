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
            if not new_state in next_states_arr:
              next_states_arr.append(new_state.copy())
    return next_states_arr

  def board_in_endgame_state(self,state_arr):
    bigger_than_one_count = 0
    for number in state_arr:
      if number > 1:
        bigger_than_one_count += 1

    return bigger_than_one_count == 1

  def is_good_move_in_endgame(self, state_arr):
    number_of_ones = 0
    for number in state_arr:
      if number > 1:
        return False
      elif number == 1:
        number_of_ones += 1

    return number_of_ones%2 == 1
    

  def play(self, state_arr):
    next_states = self.get_next_states(state_arr)
  
    for next_state in next_states:

      if self.board_in_endgame_state(state_arr):
        if self.is_good_move_in_endgame(next_state):
          return next_state
      else:
        if self.nim_sum(next_state) == 0:
          return next_state

    return next_states[0]

