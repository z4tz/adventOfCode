import numpy as np

import InputReader

class runner:
    def __init__(self):
        self.coordinates = np.array([0,0])
        self.direction = np.array([0,1])  # starts facing north
        self.locations = [np.array([0,0])]  # initialize with initial coordinates as we already visited here
        self.foundHQ = False

    def move(self, turn, distance):
        self.direction = self.direction[::-1]  # swaps over direction [0,1] -> [1,0]
        if turn is "L":
            self.direction *= np.array([-1, 1])
        else:
            self.direction *= np.array([1, -1])

        # move one block at a time to check if visited previously
        for _ in range(distance):
            self.coordinates += self.direction  # all the work for this beauty
            if not self.foundHQ:
                self.beenHere()
            self.locations.append(np.copy(self.coordinates))

    def beenHere(self):
        for location in self.locations:
            if np.array_equal(location, self.coordinates):
                print("Deja'vu after moving {0} blocks and at a distance of {1} from the start".format(len(self.locations),self.distance))
                self.foundHQ = True

    @property
    def distance(self):
        return abs(self.coordinates[0])+abs(self.coordinates[1])  # no diagonal travel allowed


def run():
    r = runner()
    data = InputReader.read('Inputs/1.txt')[0].replace(' ', '').split(',')
    for move in data:
        r.move(move[0], int(move[1:]))
    print("Total distance: {0}".format(r.distance))

    #pyplot.plot(*zip(*r.locations))
    #pyplot.show()


if __name__ == "__main__":
    run()
