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
mutation_rate = 0.001
mutation_severity = 0.05
crossover_point = 0.5
elitism_rate = 0.03
migration_rate = 0.15
reset_bottom_count = 10
current_epoch = 0 #for filename


def play_nim_game(players):
    board = [1,3,5,7]
    player_index = 0

    loser = None
    while loser == None:
        player = players[player_index]
        board = player.play(board)
        if board == [0,0,0,0]:
            loser = player
        player_index = (player_index + 1) % 3
    return loser
    


        


def get_next_states(state_arr):
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
    child = genetic_nim_player.NimPlayer()
    child.dna = combined_dna
    return child

def mutate(individual):
    for gene in individual.dna:
        if random.random() < mutation_rate:
            next_boards = get_next_states(gene.curr_board)
            random.shuffle(next_boards)
            if next_boards != None:
                gene.next_board = next_boards[0]
            else:
                gene.next_board = [0,0,0,0]

class IndividualFitness:
    def __init__(self, ind, fitness):
        self.ind = ind
        self.fitness = fitness

def determine_fitness(individual, population):
    players = [individual]
    games_played = 0
    loses = 0
    #I know this is super inefficient but I thought I had another week and cannot make it better in the short time i have to finish and train model
    for i in range(0,len(population)):
        if individual != population[i]:
            if len(players) < 3:
                players.append(population[i])

            else:
                loser_num = play_nim_game(players)
                if loser_num == 0:
                    loses +=1
                games_played +=1
                players = [individual]
    return games_played - loses





def get_next_generation(current_population):

    ind_fitness = []
    for individual in current_population:
        ind_fitness.append(IndividualFitness(individual,determine_fitness(individual, current_population)))
    #sort ind_fitness by fitness
    ind_fitness = sorted(ind_fitness, key=lambda ind_fit: ind_fit.fitness, reverse=True)
    filename = "best_dna_epoch_ " + str(current_epoch) + ".txt"
    save_dna_to_file(ind_fitness[0].ind.dna, filename)
    next_generation = []
    for i in range(int(len(ind_fitness)*elitism_rate)):
        next_generation.append(ind_fitness[i].ind)

    while len(next_generation) < generation_size - reset_bottom_count:   
        parent1 = random.choice(ind_fitness)
        parent2 = random.choice(ind_fitness)
        child = crossover(parent1.ind, parent2.ind)
        mutate(child)
        next_generation.append(child) 
    
    while len(next_generation) < generation_size:
        next_generation.append(genetic_nim_player.NimPlayer())
    return next_generation

    

def save_dna_to_file(dna, filename):
    f = open(filename, "w")
    for gene in dna:
        if gene.prev_board == None:
            f.write("None " + str(gene.curr_board) + " " + str(gene.next_board) + "\n")
        else:
            f.write(str(gene.prev_board) + " " + str(gene.curr_board) + " " + str(gene.next_board) + "\n")
    f.close()

def load_dna_from_file(filename):
    pass




population = [] #List of GeneticNimPlayer objects with no DNA
for i in range(generation_size):
    population.append(genetic_nim_player.NimPlayer())

for epoch in range(epochs):
    print("Epoch " + str(epoch))
    current_epoch = epoch #for filename
    population = get_next_generation(population)
    print()






