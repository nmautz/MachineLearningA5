
def nim_sum(state_arr):
  total = 0
  for number in state_arr:
    total ^= number
  return total


def next_states(state_arr):

  next_states_arr = []  
  for number in state_arr:
    if number > 0:
      for i in range(1, number+1):
        new_state = state_arr.copy()
        new_state[state_arr.index(number)] -= i
        next_states_arr.append(new_state)
  return next_states_arr

def is_game_won(state_arr):
  return len(next_states(state_arr)) == 0
  
