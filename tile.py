class Tile:
    def __init__(self):
        self.food = 0
        self.temperature = 0
        self.water = 0
        self.individuals = []

    def print(self):
        print(len(self.individuals))

    def insert_individual(self, ind):
        self.individuals.append(ind)

    def get_food(self):
        return self.food
    def get_temperature(self):
        return self.temperature
    def get_water(self):
        return self.water
    def get_individuals(self):
        return self.individuals
    def get_ids(self):
        arr = []
        for ind in self.individuals:
            arr.append(ind.id)
        return arr

    def set_food(self, inp):
        self.food = inp
    def set_temperature(self, inp):
        self.temperature = inp
    def set_water(self, inp):
        self.water = inp
    def set_individuals(self, inp):
        self.individuals = inp




        #self._
    #if __name__ == "__main__":
    #    tile = tile.Tile()