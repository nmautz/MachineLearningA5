

#Nathan Mautz
#10/18/23
#Nim player used for playing in competition, loads in DNA from string.
#DNA was created on 10/19/23 after 100 epochs with a generation size of 99
#DNA is stored in a string, and is parsed into a list of Gene objects.
#Each Gene object has 3 attributes:
#  prev_board: The previous board state
#  curr_board: The current board state
#  next_board: The next board state
# 
# I used "https://www.textfixer.com/tools/remove-line-breaks.php" to remove the new lines from the saved DNA to past it as a string here
#
import numpy as np
import random

class Gene:
  def __init__(self, prev_board, curr_board, next_board):
    self.prev_board = prev_board
    self.curr_board = curr_board
    self.next_board = next_board

    
dna_str = "None [1, 3, 5, 7] [1, 3, 1, 7] [1, 3, 1, 7] [1, 2, 1, 3] [1, 2, 1, 1] [1, 2, 1, 1] [0, 2, 0, 1] [0, 1, 0, 1]"



def load_dna_from_str():
  dna = []
  current_gene = []
  for gene_str in dna_str.split(" "):
    if len(current_gene) < 3:
      if gene_str != "None":
        current_gene.append(list(map(int, gene_str[1:-1].split(","))))
      else:
        current_gene.append(None)
      pass
    else:
      dna.append(Gene(current_gene[0], current_gene[1], current_gene[2]))

  return dna
      
  


class NimPlayer:
  
  def __init__(self):
    self.dna = load_dna_from_str()
    self.prev_board = None

  def add_gene(self, gene):
    self.dna.append(gene)

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

  def find_related_gene(self, prev_board, curr_board):
    for gene in self.dna:
      if gene.prev_board == prev_board and gene.curr_board == curr_board:
        return gene
    # No gene found, generate new one
    next_boards = self.get_next_states(curr_board)
    random.shuffle(next_boards)
    gene = Gene(prev_board, curr_board, [0,0,0,0])
    if next_boards != None:
      gene = Gene(prev_board, curr_board, next_boards[0])
    self.add_gene(gene) #Remember gene
    return gene


  def play(self, state_arr):
    next_board = self.find_related_gene(self.prev_board, state_arr).next_board
    self.prev_board = next_board
    return next_board

