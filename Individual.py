from __future__ import annotations
import random
import sys
import typing
from typing_extensions import Self


class Genome:

    def __init__(self: Self, traits: list|dict):
        self.genome = {}
        if(type(traits) == list):
            for t in traits:
                self.genome[t] = random.random()
        elif(type(traits) == dict):
            for t in traits:
                self.genome[t] = traits[t]

    def crossover(genome1: Genome, genome2: Genome):
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
        return Genome(new_genome)        

    def mutate(genome: Genome, mutation_rate: float = None):
        genome = genome.genome
        if(mutation_rate == None):
            mutation_rate = 1 / len(genome)
        for t in genome:
            if(random.random() <= mutation_rate):
                genome[t] = random.random()
        return Genome(genome)


    def display(self: Self):
        print(self.genome)        


class Individual:
    ids: list = []

    def __init__(self: Self, genome: Genome):
        if(genome == {}):
            sys.exit("Cannot create individual with empty genome!")
        self.genome = genome
        self.id = 0 if len(Individual.ids) == 0 else max(Individual.ids) + 1
        Individual.ids.append(self.id)

    def reproduce(self: Self, other: Individual):
        offspring_genome = Genome.mutate(Genome.crossover(self.genome, other.genome))
        offspring = Individual(offspring_genome)
        return offspring

traits = ["Move Up", "Move Down", "Move Right", "Move Left", "Sight Range", "Metabolism", "Food Preference"]
test1 = Individual(Genome(traits))
test2 = Individual(Genome(traits))
test1.genome.display()
test2.genome.display()
off1 = test1.reproduce(test2)
off1.genome.display()
print(Individual.ids)
