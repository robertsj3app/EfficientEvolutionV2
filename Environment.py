import random

from Tile import Tile
from Individual import Individual
from Individual import TraitGenome
from GUI import GUI
import time

class Environment(object):
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.grid = [[Tile((i, ii)) for ii in range(self.y)] for i in range(self.x)]
        self.current_grid = []# used to remember the grid when going back in time
        self.history = []
        self.appearance = open(r"./Appearance.txt", "w")
        self.individuals = []
        self.turn = 0
        self.last_wanted_position = (-1,-1)
        #self.label()

    def pass_time(self):
        if self.turn < len(self.history) - 1:
            self.grid = self.history[self.turn + 1]
            self.turn += 1
            return
        elif self.turn == len(self.history) - 1:
            self.grid = self.current_grid
            self.turn += 1
            return

        self.history.append([[self.grid[i][ii].copy() for ii in range(self.y)] for i in range(self.x)])

        for item in self.individuals:
            tile_list = []
            item.timeToLive -= 1
            if item.timeToLive == 0:
                self.remove_individual(item)
                self.individuals.remove(item)
                continue
            sight_range = 2
            surrounding_tiles = self.get_tiles_around(item.position, sight_range)
            #print("")
            #for til in surrounding_tiles:
            #    print(til.position)
            #print("")
            preferred_position = item.getPreferredTile(surrounding_tiles)
            # possible for loop for below line if giving a movement speed

            positions_in_range = self.get_tile_towards_tile(item.position, preferred_position)
            if len(positions_in_range) == 1:
                one_position_in_range = positions_in_range[0]
            else:
                for i in range(len(positions_in_range)):
                    tile_list.append(self.get_tile(positions_in_range[i]))
                one_position_in_range = item.getPreferredTile(tile_list)
            tile_in_range = self.grid[one_position_in_range[0]][one_position_in_range[1]]
            self.last_wanted_position = preferred_position
            self.move_one_individual(item, one_position_in_range)
            if tile_in_range.attributes['Food'] > 0:
                item.eat(tile_in_range)
        self.turn += 1

    def back_time(self):
        if self.turn == 0:
            return
        if self.turn == len(self.history):
            self.current_grid = self.grid
        print(len(self.history))
        self.grid = self.history[self.turn - 1]
        self.turn -= 1

    def insert_species(self, ind, positions):
        for pos in positions:
            self.insert_one_creature(ind.copy(), pos)

    def insert_one_creature(self, ind, position):
        self.get_tile(position).insert_individual(ind)
        self.individuals.append(ind)
        ind.position = position

    def remove_individual(self, ind):
        pos = ind.position
        self.grid[pos[0]][pos[1]].remove_individual(ind)

    def move_one_individual(self, ind, new_pos):
        self.get_tile(new_pos).insert_individual(ind)
        self.get_tile(ind.position).remove_individual(ind)
        ind.position = new_pos

    # returns an array of tiles. If length is one, creature moves there
    # if length is two, creature must decide which tile to go to
    def get_tile_towards_tile(self, old_pos, new_pos):
        x_movement = new_pos[0] - old_pos[0]
        y_movement = new_pos[1] - old_pos[1]
        tile_list = []
        if (x_movement == 0) and (y_movement == 0):
            return [old_pos]
        if abs(x_movement) > abs(y_movement):
            if x_movement > 0:
                return [(old_pos[0]+1, old_pos[1])]
            if x_movement < 0:
                return [(old_pos[0]-1, old_pos[1])]
            if x_movement == 0:
                print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                return [old_pos]
        if abs(x_movement) < abs(y_movement):
            if y_movement > 0:
                return [(old_pos[0], old_pos[1]+1)]
            if y_movement < 0:
                return [(old_pos[0], old_pos[1]-1)]
            if y_movement == 0:
                print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                return [old_pos]
        if abs(x_movement) == abs(y_movement):
            # creature does not know to go vertical or horizontal
            if x_movement > 0:
                tile_list.append((old_pos[0]+1, old_pos[1]))
            elif x_movement < 0:
                tile_list.append((old_pos[0]-1, old_pos[1]))
            else:
                print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                return [old_pos]
            if y_movement > 0:
                tile_list.append((old_pos[0], old_pos[1]+1))
            elif y_movement < 0:
                tile_list.append((old_pos[0], old_pos[1]-1))
            else:
                print("UNEXPECTED RESULT IN GET_TILE_TOWARDS_TILE")
                return [old_pos]
            return tile_list
        return [old_pos]


    #testing needed
    def get_tiles_around(self, position, sight_range):
        tiles = []
        for i in range(1 + (sight_range * 2)):
            for ii in range(1 + (sight_range * 2)):
                temp_tile = self.get_tile((position[0] - sight_range + i, position[1] - sight_range + ii))
                if temp_tile is not None:
                    tiles.append(temp_tile)
                #print(str(position[0] - sight_range + i) + ", " + str(position[0] - sight_range + ii))
        return tiles

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
                to_print += "" + str(len(item.individuals)) + "  "
            print(to_print)

    def print_attributes_to_file(self):
        for row in range(self.x):
            for col in range(self.y):
                self.appearance.write("Position:     (" + str(self.grid[row][col].position[0]) + "," + str(self.grid[row][col].position[1]) + ")")
                self.appearance.write("\nResidents:    " + str(self.grid[row][col].individuals))
                self.appearance.write("\nResident IDs: " + str(self.grid[row][col].get_ids()))
                for key in self.grid[0][0].attributes:
                    self.appearance.write(f"{key}: {self.grid[row][col].attributes[key]}")
                self.appearance.write("\n\n")
        self.appearance.write("\n\n")
        self.appearance.close()
        print('hi')

