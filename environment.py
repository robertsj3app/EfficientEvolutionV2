from tile import Tile

class Environment(object):
    def __init__(self):
        self._grid = [[Tile() for i in range(2)] for ii in range(2)]
        self._appearance = open(r"./Appearance.txt", "w")

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