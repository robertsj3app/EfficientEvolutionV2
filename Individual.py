from __future__ import annotations
import random
import sys
from turtle import shape
from typing_extensions import Self
from matplotlib.pyplot import rc
from numpy import random
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from keras.models import Sequential
from keras.layers import Input, Dense
from math import prod

class Brain:

    def __init__(self: Self):
        self.network = Sequential()
        self.network.add(Input(8))
        self.network.add(Dense(7, activation='relu'))
        self.network.add(Dense(15, activation='relu'))
        self.network.add(Dense(8, activation='sigmoid'))

    def to_genome(self: Self):
        shapes = []
        genome = []
        for l in self.network.get_weights():
            shapes.append(l.shape)
            genome = np.concatenate([genome, l.flatten()])
        
        return BrainGenome(genome, shapes)

class BrainGenome:
    def __init__(self: Self, weights: list, shapes: list):
        self.genome = weights
        self.shapes = shapes

    def crossover(genome1: BrainGenome, genome2: BrainGenome):
        genome01 = genome1.genome
        genome02 = genome2.genome
        if(genome1.shapes != genome2.shapes):
            sys.exit("These two genomes are incompatible and cannot be crossed over.")
        new_genome = []
        for i in range(len(genome01)):
            if(random.random() > 0.5):
                new_genome.append(genome01[i])
            else:
                new_genome.append(genome02[i])
        return BrainGenome(new_genome, genome1.shapes)

    def to_weights(self: Self):
        layer_weights = []
        genome = self.genome
        for w in self.shapes:
            flattened_arr = genome[:prod(w)]
            genome = genome[prod(w):]
            layer_weights.append(np.reshape(flattened_arr, w))
            
        return layer_weights

    # def mutate(genome: Genome, mutation_rate: float = None, mutation_amount: float = 0.33):
    #     genome = genome.genome
    #     if(mutation_rate == None):
    #         mutation_rate = 1 / len(genome)
    #     for t in genome:
    #         if(random.random() <= mutation_rate):
    #             genome[t] = genome[t] + random.normal(genome[t], mutation_amount) if random.random() <= 0.5 else genome[t] - random.normal(genome[t], mutation_amount)
    #             #if(genome[t] < 0):
    #             #    genome[t] = 0
    #             #elif(genome[t] > 1):
    #             #    genome[t] = 1
    #     return Genome(genome)


    def display(self: Self):
         print(self.genome + "\n" + self.shapes)


class TraitGenome:

    def __init__(self: Self, traits: list|dict):
        self.genome = {}
        self.shape = ()
        if(type(traits) == list):
            for t in traits:
                self.genome[t] = random.random()
        elif(type(traits) == dict):
            for t in traits:
                self.genome[t] = traits[t]

    def crossover(genome1: TraitGenome, genome2: TraitGenome):
        genome1 = genome1.genome
        genome2 = genome2.genome
        if(genome1.keys() != genome2.keys()):
            sys.exit("These two genomes are incompatible and cannot be crossed over.")
        new_genome = {}
        for t in genome1:
            if(random.random() > 0.5):
                new_genome[t] = genome1[t]
            else:
                new_genome[t] = genome2[t]
        return TraitGenome(new_genome)        

    def mutate(genome: TraitGenome, mutation_rate: float = None, mutation_amount: float = 0.33):
        genome = genome.genome
        if(mutation_rate == None):
            mutation_rate = 1 / len(genome)
        for t in genome:
            if(random.random() <= mutation_rate):
                genome[t] = genome[t] + random.normal(genome[t], mutation_amount) if random.random() <= 0.5 else genome[t] - random.normal(genome[t], mutation_amount)
                if(genome[t] < 0):
                    genome[t] = 0
                elif(genome[t] > 1):
                    genome[t] = 1
        return TraitGenome(genome)


    def display(self: Self):
        print(self.genome)        


class Individual:
    ids: list = []

    def __init__(self: Self, genome: TraitGenome, bgenome: BrainGenome = None):
        if(genome == {}):
            sys.exit("Cannot create individual with empty genome!")
        self.genome = genome
        self.brain = Brain()
        if(bgenome != None):
            self.brain.network.set_weights(bgenome.to_weights())
        self.id = 0 if len(Individual.ids) == 0 else max(Individual.ids) + 1
        Individual.ids.append(self.id)
        self.position = (-1, -1)

    def reproduce(self: Self, other: Individual):
        offspring_genome = TraitGenome.mutate(TraitGenome.crossover(self.genome, other.genome))
        offspring = Individual(offspring_genome)
        return offspring

    def get_id(self: Self):
        return self.id

b1 = Brain()
b2 = Brain()
bg1 = b1.to_genome()
bg2 = b2.to_genome()
bgo = BrainGenome.crossover(bg1, bg2)

with(open("bg1.txt", "w+")) as w:
    print(bg1.genome, file=w)

with(open("bg2.txt", "w+")) as g:
    print(bg2.genome, file=g)

with(open("bgo.txt", "w+")) as rw:
    print(bgo.genome, file=rw)
