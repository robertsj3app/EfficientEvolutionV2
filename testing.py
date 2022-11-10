from Environment import Environment
from GUI import GUI
from Tile import Tile
from Individual import Brain
from Individual import BrainGenome
from Individual import TraitGenome
from Individual import Individual
import time

#more testing
#implement logic more in environment
#keeping a list of all past times
#improve GUI


#b1 = Brain()
#b2 = Brain()
#b3 = Brain(BrainGenome.mutate(BrainGenome.crossover(b1.to_genome(), b2.to_genome())))
#tiles = [Tile((0, 0)), Tile((0, 1)), Tile((0, 2))]
#tiles[0].attributes["Water"] = 3
#tiles[0].position = (1,0)
#tiles[1].attributes["Food"] = 4
#tiles[1].position = (2,0)
#tiles[2].individuals = [0,0,0,0,0]
#tiles[2].position = (3,0)
#outputs = b1.getPreferredTile(tiles, show_outputs=True)
#print(outputs)
#outputs = b2.getPreferredTile(tiles, show_outputs=True)
#print(outputs)
#outputs = b3.getPreferredTile(tiles, show_outputs=True)
#print(outputs)

#env = Environment()
#gui = GUI(env)
#traits = ["Move Up", "Move Down", "Move Right", "Move Left", "Sight Range", "Metabolism", "Food Preference"]
#ind = Individual(TraitGenome(traits))
#env.insert_one_creature(ind, (0,0))
#gui.make_grid()
#ks = ind.genome.genome.keys()
##env.print_attributes_to_file()
#env.get_tiles_around((0,0), 2)
#env.move_one_individual(env.get_tile((0,0)).individuals[0], env.get_tile_towards_tile((0,0), (1,0)))
#env.insert_one_creature(ind, (2, 2))
#time.sleep(1)
#gui.make_grid()
#env.print_attributes_to_file()
#gui.mainloop()

traits = ["Move Up", "Move Down", "Move Right", "Move Left", "Sight Range", "Metabolism", "Food Preference"]
ind = Individual(TraitGenome(traits))

env = Environment(4,5)

i = 0
for row in env.grid:
    for item in row:
        item.attributes['Food'] = i
        i += 1
gui = GUI(env)
env.insert_one_creature(ind, (0,0))
env.move_one_individual(ind, (3, 4))
gui.make_grid()
gui.mainloop()