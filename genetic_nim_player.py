#Nathan Mautz
#10/18/23
#Nim player used for training in genetic_trainer.py. Has no DNA
import numpy as np
import random

class Gene:
  def __init__(self, prev_board, curr_board, next_board):
    self.prev_board = prev_board
    self.curr_board = curr_board
    self.next_board = next_board

    



class NimPlayer:
  
  def __init__(self):
    self.dna = []
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
    next_boards = random.shuffle(next_boards)
    gene = Gene(prev_board, curr_board, next_boards[0])
    self.add_gene(gene) #Remember gene
    return gene


  def play(self, state_arr):
    return self.find_related_gene(self.prev_board, state_arr).next_board

