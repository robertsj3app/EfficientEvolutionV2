from Environment import Environment
from GUI import GUI
from Tile import Tile
from Individual import Brain
from Individual import BrainGenome
from Individual import TraitGenome
from Individual import Individual
import time
from StartGUI import StartGUI

#more testing
#implement logic more in environment
#keeping a list of all past times
#improve GUI

#traits = ["Move Up", "Move Down", "Move Right", "Move Left", "Sight Range", "Metabolism", "Food Preference"]
#traits2 = ["Move Up", "Move Down", "Move Right", "Move Left", "Sight Range", "Metabolism", "Food Preference"]
#traits3 = ["Move Up", "Move Down", "Move Right", "Move Left", "Sight Range", "Metabolism", "Food Preference"]
#ind = Individual(TraitGenome(traits))
#ind2 = Individual(TraitGenome(traits2))
#ind3 = Individual(TraitGenome(traits3))
#til = Tile((7,8))

#ind1 = ind.copy()

sg = StartGUI()
sg.mainloop()

#env = Environment(4,5)

#i = 0
#for row in env.grid:
#    for item in row:
#        item.attributes['Food'] = i
#        i += 1

#env.grid[2][3].attributes['Food'] = 0
#env.grid[2][3].attributes['Hazard'] = 1

#env.grid[1][1].attributes['Food'] = 0
#env.grid[1][1].attributes['Water'] = 1

#gui = GUI(env)
#env.insert_one_creature(ind, (0,0))
#env.move_one_individual(ind, (3, 4))
#env.insert_one_creature(ind2, (1, 1))
#env.insert_one_creature(ind3, (2, 1))
#gui.make_grid()
#gui.mainloop()
