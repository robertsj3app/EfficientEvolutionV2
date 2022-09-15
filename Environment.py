import random

from Tile import Tile
from Individual import Individual
from Individual import Genome

class Environment(object):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.grid = [[Tile() for i in range(self.x)] for ii in range(self.y)]
        self.appearance = open(r"./Appearance.txt", "w")


    def insert_species(self, ind, positions):
        for pos in positions:
            self.insert_one_creature(ind.copy(), pos)

    def insert_one_creature(self, ind, position):
        self.get_tile(position).insert_individual(ind)
        ind.position = position

    #def pass_time:

    def move_one_individual(self, ind, new_pos):
        self.get_tile(new_pos).insert_individual(ind)
        self.get_tile(ind.position).remove_individual(ind)
        ind.position = new_pos

    def get_tile_towards_tile(self, old_pos, new_pos):
        x_movement = new_pos[0] - old_pos[0]
        y_movement = new_pos[1] - old_pos[1]
        if (x_movement == 0) and (y_movement == 0):
            return old_pos
        if abs(x_movement) > abs(y_movement):
            if x_movement > 0:
                return (old_pos[0]+1, old_pos[1])
            if x_movement < 0:
                return (old_pos[0]-1, old_pos[1])
            if x_movement == 0:
                print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                return old_pos
        if abs(x_movement) < abs(y_movement):
            if y_movement > 0:
                return (old_pos[0], old_pos[1]+1)
            if y_movement < 0:
                return (old_pos[0], old_pos[1]-1)
            if y_movement == 0:
                print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                return old_pos
        if abs(x_movement) == abs(y_movement):
            num = int(random.random() * 2)
            if num == 0:
                if x_movement > 0:
                    return (old_pos[0]+1, old_pos[1])
                if x_movement < 0:
                    return (old_pos[0]-1, old_pos[1])
                if x_movement == 0:
                    print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                    return old_pos
            if num == 1:
                if y_movement > 0:
                    return (old_pos[0], old_pos[1]+1)
                if y_movement < 0:
                    return (old_pos[0], old_pos[1]-1)
                if y_movement == 0:
                    print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                    return old_pos
        return old_pos

    def get_tiles_around(self, position, sight_range):
        tiles = []
        for i in range(1 + (sight_range * 2)):
            for ii in range(1 + (sight_range * 2)):
                temp_tile = self.get_tile((position[0] - sight_range + i, position[0] - sight_range + ii))
                if temp_tile is not None:
                    tiles.append((temp_tile, 0))
                #print(str(position[0] - sight_range + i) + ", " + str(position[0] - sight_range + ii))
        return tiles

    #ind = individual
    #tiles = (Tile, int)
    def get_favorable_tile(self, ind, tiles):
        return ind.get_favorable_tile(tiles)
#        temp_names = list(ind.genome.genome.keys())
#        temp_genes = ind.genome.genome.keys()
#        for i in range(ind.genome.genome.keys()):
#            if "movement" in temp_names[i]:
#                for tile in tiles:
#                    if "water" in temp_names[i]:
#                        if tile[0].get_water() >= 1:
#                            tile[1] += temp_genes[i]
#                    elif "social" in temp_names[i]:
#                       if len(tile[0].get_individuals()) > 0:
#                            tile[1] += temp_genes[i]
                #here, consider making another class with the purpose of connecting genes to tile attributes
#        return tiles

    def get_tile(self, position):
        if position[0] < 0 or position[0] >= self.x:
            return None
        if position[1] < 0 or position[1] >= self.y:
            return None
        return self.grid[position[0]][position[1]]

    def print_grid(self):
        for row in range(len(self.grid)):
            to_print = ""
            for item in self.grid[row]:
                to_print += item.get_individuals() + " "
            print(to_print)

    def print_attributes_to_file(self):
        for row in range(self.x):
            to_print = ""
            i = 0
            for item in self.grid[row]:
                self.appearance.write("Position:     (" + str(row) + "," + str(i) + ")")
                self.appearance.write("\nResidents:    " + str(item.individuals))
                self.appearance.write("\nResident IDs: " + str(item.get_ids()))
                self.appearance.write("\nFood:         " + str(item.food))
                self.appearance.write("\nWater:        " + str(item.water))
                self.appearance.write("\nTemperature:  " + str(item.temperature))
                self.appearance.write("\n\n")
                i += 1
        self.appearance.write("\n\n")


env = Environment()
traits = ["Move Up", "Move Down", "Move Right", "Move Left", "Sight Range", "Metabolism", "Food Preference"]
ind = Individual(Genome(traits))
env.insert_one_creature(ind, (0,0))
print(type(ind.genome.genome.keys()))
ks = ind.genome.genome.keys()
print(f"KEYS: {list(ks)[0]}")
#env.print_grid()
env.print_attributes_to_file()
env.get_tiles_around((0,0), 2)

env.move_one_individual(env.get_tile((0,0)).individuals[0], env.get_tile_towards_tile((0,0), (1,0)))

env.print_attributes_to_file()

print(env.get_tile((1,0)).individuals[0].position)


#if gene is movement decider
##    for loop to go through all those genes
#     each gene is going to add favorability to each tile