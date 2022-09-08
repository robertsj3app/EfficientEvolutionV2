class Tile:
    def __init__(self):
        self._food = 0
        self._temperature = 0
        self._water = 0
        self._individuals = []

    def print(self):
        print("OO")

    def get_food(self):
        return self._food
    def get_temperature(self):
        return self._temperature
    def get_water(self):
        return self._water
    def get_individuals(self):
        return self._individuals

    def set_food(self, inp):
        self._food = inp
    def set_temperature(self, inp):
        self._temperature = inp
    def set_water(self, inp):
        self._water = inp
    def set_individual(self, inp):
        self._individuals = inp



        #self._
    #if __name__ == "__main__":
    #    tile = tile.Tile()