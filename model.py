
def nim_sum(numbers):
  total = 0
  for number in numbers:
    total ^= number
  return total


def calculate_heuristic_score(state):
  return nim_sum(state)

class Node:
  
  def __init__(self, state, parent_node):
    self.state = state
    self.parent_node = parent_node
    if parent_node != None:
      self.g = parent_node.g +1
    else: 
      self.g = 0
    self.h = calculate_heuristic_score(state)
    self.f = self.g + self.h

