class Tile:
    def __init__(self, pos):
        self.attributes = ["Food", "Temperature", "Water"]
        self.weights = [0, 0, 0]
        self.food = 0
        self.temperature = 0
        self.water = 0
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
        str = str + f"Position: {self.position[0]} , {self.position[1]}\n"
        for i in range(len(self.attributes)):
            str = str + f"{self.attributes[i]}: {self.weights[i]}\n"
        str = str + "\nInhabitants:\n"
        for item in self.individuals:
            str = str + f'{item.id}'
            str = str + '\n'
        return str


#modifiability
#creature genome
#what is in a tile