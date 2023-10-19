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






