#Nathan Mautz
#09/29/23
#Nim player that calculates all possible moves and plays the first one.
import numpy as np
class NimPlayer:
  
  def __init__(self):
    pass

  def is_game_won(self, state_arr):
    return sum(state_arr) == 1
    
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
    

  def minimax(self, state_arr, depth, maximizing_player, is_end_game):


    if depth == 0:
      if is_end_game:
        if not self.is_good_move_in_endgame(state_arr):
          if maximizing_player:
            return 1
          else:
            return -1
        else:
          if maximizing_player:
            return -1
          else:
            return 1
      else:
        if self.nim_sum(state_arr) == 0:
          if maximizing_player:
            return -1
          else:
            return 1
        else:
          if maximizing_player:
            return 1
          else:
            return -1
    
    if maximizing_player:
      best_value = -np.inf
      for next_state in self.get_next_states(state_arr):
        value = self.minimax(next_state, depth-1, False, self.board_in_endgame_state(state_arr))
        best_value = max(best_value, value)
      return best_value
    
    else:
      best_value = np.inf
      for next_state in self.get_next_states(state_arr):
        value = self.minimax(next_state, depth-1, True, self.board_in_endgame_state(state_arr))
        best_value = min(best_value, value)
      return best_value




  def play(self, state_arr):
    next_states = self.get_next_states(state_arr)

    best_state = None
    best_value = -np.inf
    for next_state in next_states:
      value = self.minimax(next_state, 0, False, self.board_in_endgame_state(state_arr))
      if value > best_value:
        best_state = next_state
        best_value = value
    if best_state is not None:
      return best_state
    return next_states[0]

