from tile import Tile

class Environment(object):
    def __init__(self):
        self._x = 4
        self._y = 3
        self._grid = [[Tile() for i in range(self._x)] for ii in range(self._y)]
        self._appearance = open(r"./Appearance.txt", "w")

    #def pass_time:

#    def move_one_individual(self, ind):
#        for gene in ind.get_genome():
#            if gene[1] == "movement":
#                for tile in

    def get_tiles_around(self, position, range):
        tiles = []
        for i in range(3):
            for ii in range(3):
                temp_tile = self.get_tile((position[0] - (3/3) + i, position[0] - (3/3) + ii))


    def get_tile(self, position):
        if position[0] < 0 or position[0] >= self._x:
            return None
        if position[1] < 0 or position[1] >= self._y:
            return None
        return self._grid[position[0]][position[1]]


    def print_grid(self):
        for row in range(len(self._grid)):
            to_print = ""
            for item in self._grid[row]:
                to_print += item.get_individual() + " "
            print(to_print)

    def print_attributes_to_file(self):
        for row in range(len(self._grid)):
            to_print = ""
            i = 0
            for item in self._grid[row]:
                self._appearance.write("Position:    (" + str(row) + "," + str(i) + ")")
                self._appearance.write("\nResident:    " + str(item.get_individual()))
                self._appearance.write("\nFood:        " + str(item.get_food()))
                self._appearance.write("\nWater:       " + str(item.get_water()))
                self._appearance.write("\nTemperature: " + str(item.get_temperature()))
                self._appearance.write("\n\n")
                i += 1
env = Environment()
env.print_grid()
env.print_attributes_to_file()


#if gene is movement decider
##    for loop to go through all those genes
#     each gene is going to add favorability to each tile