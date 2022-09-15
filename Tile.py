class Tile:
    def __init__(self):
        self.food = 0
        self.temperature = 0
        self.water = 0
        self.individuals = []
        self.position = (-1, -1)

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

        #self._
    #if __name__ == "__main__":
    #    tile = tile.Tile()