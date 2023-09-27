import heapq

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

  def __lt__(self, other):
    return self.f < other.f
  
  def __gt__(self, other):
    return self.f > other.f
  

class AStar:

  def __init__(self, start_state):
    self.nodes_to_visit = [Node(start_state, None)]
    heapq.heapify(self.nodes_to_visit)
    
  def expand_node(self, node):
    #add all possible next states to self.tovisit
    for number in node.state:
      if number > 0:
        for i in range(1, number+1):
          new_state = node.state.copy()
          new_state[node.state.index(number)] -= i
          heapq.heappush(self.nodes_to_visit, Node(new_state, node))

  


  def run(self):
    while self.nodes_to_visit:
      node = heapq.heappop(self.nodes_to_visit)
      if nim_sum(node.state) == 0:
        return node
      self.expand_node(node)

state = [1,2,3]
model = AStar(state)
model.expand_node(Node(state, None))
for node in model.nodes_to_visit:
  print(node.state)