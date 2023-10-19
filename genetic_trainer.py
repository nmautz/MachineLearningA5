import copy
import random
import traceback
import time
import sys
import numpy as np



try:
    import genetic_nim_player
    print("Loaded genetic_nim_player.py")
except:
    print("Couldn't find genetic_nim_player.py")
  


generation_size = 99
communities = 4
epochs = 100
mutation_rate = 0.1
mutation_severity = 0.05
crossover_point = 0.5
elitism_rate = 0.03
migration_rate = 0.15
reset_bottom_rate = 0.1


def crossover(parent1, parent2):
    pass

def mutate(individual):
    pass

def get_next_generation(current_population):
    pass

def save_dna_to_file(dna, filename):
    pass

def load_dna_from_file(filename):
    pass







