import copy

class Tile:
    def __init__(self, pos):
        self.attributes = {"Food": 0, "Hazard": 0, "Water": 0}
        self.individuals = []
        self.position = pos

    def print(self):
        print(len(self.individuals))

    def insert_individual(self, ind):
        self.individuals.append(ind)

    def remove_individual(self, ind):
        self.individuals.remove(ind)

    def get_ids(self):
        id_list = []
        for item in self.individuals:
            id_list.append(item.id)
        return id_list

    def get_num_individuals(self):
        return len(self.individuals)

    def get_description(self):
        str = ""
        str = str + f"Position: {self.position}\n"
        for key in self.attributes:
            str = str + f"{key}: {self.attributes[key]}\n"
        str = str + "\nInhabitants:\n"
        for item in self.individuals:
            str = str + f'{item.id} ({item.gender}): Lifespan = {item.timeToLive}'
            str = str + '\n'
        return str

    def copy(self):
        new_tile = Tile(self.position)
        new_tile.attributes = copy.deepcopy(self.attributes)
        new_inds = []
        for ind in self.individuals:
            new_inds.append(ind.copy())
        new_tile.individuals = new_inds
        return new_tile

    def copy_empty(self):
        new_tile = Tile(self.position)
        new_tile.attributes = copy.deepcopy(self.attributes)
        return new_tile

#modifiability
#creature genome
#what is in a tile