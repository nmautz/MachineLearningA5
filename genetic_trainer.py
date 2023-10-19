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

def crossover(parent1, parent2):
    parent1_dna = parent1.dna
    parent2_dna = parent2.dna
    combined_dna = parent1_dna + parent2_dna
    for gene in combined_dna:
        for gene2 in combined_dna:
            if gene.prev_board == gene2.prev_board and gene.curr_board == gene2.curr_board:
                combined_dna.remove(gene2)
    child = genetic_nim_player.GeneticNimPlayer()
    child.dna = combined_dna

def mutate(individual):
    for gene in individual.dna:
        if random.random() < mutation_rate:
            next_boards = get_next_states(gene.curr_board)
            next_boards = random.shuffle(next_boards)
            gene.next_board = next_boards[0]

def get_next_generation(current_population):
    pass

def save_dna_to_file(dna, filename):
    pass

def load_dna_from_file(filename):
    pass

def determine_fitness(individual, population):
    pass


population = [] #List of GeneticNimPlayer objects with no DNA
for i in range(generation_size):
    population.append(genetic_nim_player.GeneticNimPlayer())

for epoch in range(epochs):
    print("Epoch " + str(epoch))
    for individual in population:
        individual.play_game(communities)
    population = sorted(population, key=lambda individual: individual.get_fitness(), reverse=True)
    print("Best Fitness: " + str(population[0].get_fitness()))
    population = get_next_generation(population)
    print()






