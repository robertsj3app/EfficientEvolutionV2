from tile import Tile
from Individual import Individual
from Individual import Genome

class Environment(object):
    def __init__(self):
        self._x = 2
        self._y = 2
        self._grid = [[Tile() for i in range(self._x)] for ii in range(self._y)]
        self._appearance = open(r"./Appearance.txt", "w")


    def insert_species(self, ind, positions):
        for pos in positions:
            self.insert_one_creature(ind.copy(), pos)

    def insert_one_creature(self, ind, position):
        self.get_tile(position).insert_individual(ind)

    #def pass_time:

    def move_one_individual(self, ind, new_pos):
        self.get_tile(new_pos).insert_individual(ind)
        self.get_tile(ind.get_position()).remove_individual(ind)
        
        #tiles = self.get_tiles_around(ind.get_position(), ind.get_sight_range())
        #tiles = self.set_favorability(ind, tiles)
        #best_tiles = []
        #best_tile = tiles[0][0]
       # for i in range(len(tiles)):
       #     if tiles[i][1] >


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
        return ind.get_favorable_tile(ind, tiles)
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
        if position[0] < 0 or position[0] >= self._x:
            return None
        if position[1] < 0 or position[1] >= self._y:
            return None
        return self._grid[position[0]][position[1]]

 #   def print_grid(self):
 #       for row in range(len(self._grid)):
 #           to_print = ""
 #           for item in self._grid[row]:
 #               to_print += item.get_individuals() + " "
 #           print(to_print)

    def print_attributes_to_file(self):
        for row in range(self._x):
            to_print = ""
            i = 0
            for item in self._grid[row]:
                self._appearance.write("Position:     (" + str(row) + "," + str(i) + ")")
                self._appearance.write("\nResidents:    " + str(item.get_individuals()))
                self._appearance.write("\nResident IDs: " + str(item.get_ids()))
                self._appearance.write("\nFood:         " + str(item.get_food()))
                self._appearance.write("\nWater:        " + str(item.get_water()))
                self._appearance.write("\nTemperature:  " + str(item.get_temperature()))
                self._appearance.write("\n\n")
                i += 1


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


#if gene is movement decider
##    for loop to go through all those genes
#     each gene is going to add favorability to each tile