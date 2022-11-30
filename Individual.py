from __future__ import annotations
import random
import sys
from typing_extensions import Self
from numpy import random
import numpy as np
from Tile import Tile

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

from keras.models import Sequential
from keras.layers import Input, Dense
from math import prod

class Brain:

    def __init__(self: Self, genome: BrainGenome = None) -> Brain:
        t = Tile((-1, -1))
        self.network = Sequential()
        self.network.add(Input(len(t.attributes.keys())))
        self.network.add(Dense(4, activation='relu'))
        self.network.add(Dense(4, activation='relu'))
        self.network.add(Dense(1, activation='linear'))

        if(genome != None):
            self.network.set_weights(genome.to_weights())

    def to_genome(self: Self) -> BrainGenome:
        shapes = []
        genome = []
        for l in self.network.get_weights():
            shapes.append(l.shape)
            genome = np.concatenate([genome, l.flatten()])
        
        return BrainGenome(genome, shapes)

    def getPreferredTile(self: Self, tiles: list[Tile], show_outputs: bool = False) -> tuple[int]:
        inputs = [[t.attributes["Food"], t.attributes["Hazard"], t.attributes["Water"]] for t in tiles]
        outputs = list(self.network.predict(inputs).flatten())
        if(show_outputs == True):
            print(outputs)
            
        return tiles[outputs.index(max(outputs))].position

class BrainGenome:
    def __init__(self: Self, weights: list, shapes: list) -> BrainGenome:
        self.genome = weights
        self.shapes = shapes

    def crossover(genome1: BrainGenome, genome2: BrainGenome) -> BrainGenome:
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

    def to_weights(self: Self) -> list[float]:
        layer_weights = []
        genome = self.genome
        for w in self.shapes:
            flattened_arr = genome[:prod(w)]
            genome = genome[prod(w):]
            layer_weights.append(np.reshape(flattened_arr, w))
            
        return layer_weights

    def mutate(genome: BrainGenome, mutation_rate: float = None, mutation_amount: float = 0.33) -> BrainGenome:
        if(mutation_rate == None):
            mutation_rate = 1 / len(genome.genome)
        new_genome = []
        for t in genome.genome:
            if(random.random() <= mutation_rate):
                new_genome.append(t + random.normal(t, mutation_amount) if random.random() <= 0.5 else t - random.normal(t, mutation_amount))
            else:
                new_genome.append(t)
        return BrainGenome(new_genome, genome.shapes)

    def display(self: Self):
         print(self.genome + "\n" + self.shapes)

class TraitGenome:

    def __init__(self: Self, traits: list|dict) -> TraitGenome:
        self.genome = {}
        self.shape = ()
        if(type(traits) == list):
            for t in traits:
                self.genome[t] = random.random()
        elif(type(traits) == dict):
            for t in traits:
                self.genome[t] = traits[t]

    def crossover(genome1: TraitGenome, genome2: TraitGenome) -> TraitGenome:
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

    def mutate(genome: TraitGenome, mutation_rate: float = None, mutation_amount: float = 0.33) -> TraitGenome:
        genome = genome.genome.copy()
        if(mutation_rate == None):
            mutation_rate = 1 / len(genome.genome)
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

    def __init__(self: Self, genome: TraitGenome, bgenome: BrainGenome = None, copy: bool = False, gender: str = None,) -> Individual:
        if not copy:
            self.genome = genome
            self.gender = gender
            self.brain = Brain(bgenome)
            self.id = 0 if len(Individual.ids) == 0 else max(Individual.ids) + 1
            self.position = (-1,-1)
            self.timeToLive = 10
            self.score = 0
            Individual.ids.append(self.id)
        else: # shallow copy an individual
            self.genome = None
            self.brain = None
            self.id = 0
            self.position = (-1, -1)
            self.timeToLive = 0
            self.score = 0

    def getPreferredTile(self: Self, tiles: list[Tile]) -> tuple[int]:
        return self.brain.getPreferredTile(tiles)

    def eat(self: Self, tile: Tile) -> None:
        self.timeToLive += 5
        tile.attributes['Food'] -= 1

    def reproduce(self: Self, other: Individual) -> Individual:
        offspring_genome = TraitGenome.mutate(TraitGenome.crossover(self.genome, other.genome))
        offspring_brain_genome = BrainGenome.mutate(BrainGenome.crossover(self.brain.to_genome(), other.brain.to_genome()))
        offspring = Individual(offspring_genome, offspring_brain_genome)
        return offspring

    def get_id(self: Self) -> int:
        return self.id

    def copy(self: Self) -> Individual:
        new_individual = Individual(genome = None, bgenome = None, copy = True)
        new_individual.genome = None
        new_individual.brain = None
        new_individual.id = self.id
        new_individual.position = self.position
        new_individual.timeToLive = self.timeToLive
        new_individual.score = self.score
        return new_individual

class Generation():

    traits = ["Sight Range", "Metabolism", "Food Preference"]
    
    def __init__(self: Self, size: int = 10, individuals: list[Individual] = None):
        self.living_individuals = []
        self.dead_individuals = []
        if(individuals != None):
            self.living_individuals = individuals
        for i in range(0, size - len(self.living_individuals)):
            self.living_individuals.append(Individual(TraitGenome(Generation.traits)))

    def get_best_scorers(self: Self, percent: float, gendered: bool = False):
        number = int(percent * len(self.dead_individuals))
        best_scorers = []
        if(gendered == False):
            sorteds = sorted(self.dead_individuals, key=lambda x: x.score, reverse=True)
            best_scorers = sorteds[:number]
        else:
            sortedsMale = sorted([s for s in self.dead_individuals if s.gender == 'm'], key=lambda x: x.score, reverse=True)
            sortedsFemale = sorted([s for s in self.dead_individuals if s.gender == 'f'], key=lambda x: x.score, reverse=True)
            best_scorers = sortedsMale[:int(number / 2)] + sortedsFemale[:int(number / 2)]
       
        return best_scorers

    def reproduce(self: Self, size: int, percent: float, gendered: bool = False):
        best_scorers = self.get_best_scorers(percent, gendered)
        new_generation = []
        for i in range(1,size):
            if(gendered == False):
                new_generation.append(random.choice(best_scorers).reproduce(random.choice(best_scorers)))
            else:
                new_generation.append(random.choice([s for s in best_scorers if s.gender == 'm']).reproduce(random.choice([s for s in best_scorers if s.gender == 'f'])))

        return Generation(size=size, individuals=new_generation)