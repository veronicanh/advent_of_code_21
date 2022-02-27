class DumboOctopus:
    def __init__(self, energy):
        self._energy = energy
        self._lastFlash = -1

    def __str__(self):
        if self._energy == 0:
            return "*"
        return str(self._energy)

    # Cant increase energy in this step if it already flashed
    def increaseEnergy(self, step):
        if (self._lastFlash != step):
            self._energy += 1

    # Only flashes max once per step
    def flashes(self, step):
        if (self._lastFlash == step):
            return False

        if (self._energy > 9):
            self._energy = 0
            self._lastFlash = step
            return True




class Grid:
    def __init__(self, file):
        self._grid = self._readFile(file)

    def __str__(self):
        prettyStr = ""
        for row in self._grid:
            for octopus in row:
                prettyStr += str(octopus) + ""
            prettyStr += "\n"
        return prettyStr

    def _readFile(self, file):
        map = []
        for line in open(file):
            map.append([DumboOctopus(int(x)) for x in line.strip()])
        return map

    def simulateFlashing(self, steps):
        #print("Before any steps:")
        #input(self)
        flashes = 0
        step = 0

        while flashes != (len(self._grid) * len(self._grid[0])):
            flashes = 0
            step += 1
            for rad in range(len(self._grid)):
                for kol in range(len(self._grid[rad])):
                    flashes += self._updateOctopus(rad, kol, step)

        print("At step " + str(step) + " all flashed simultaneously")


    def _updateOctopus(self, rad, kol, step):
        flashes = 0

        octopus = self._grid[rad][kol]
        octopus.increaseEnergy(step)

        if (octopus.flashes(step)):
            flashes += 1
            for neigbour in self._findAdjacent(rad, kol):
                flashes += self._updateOctopus(neigbour[0], neigbour[1], step)

        return flashes

    def _findAdjacent(self, rad, kol):
        adjc = []
        for rDiff in range(-1, 2):
            for kDiff in range(-1, 2):
                r = rad + rDiff
                k = kol + kDiff

                valid = True
                if ((r == rad) and (k == kol)):
                    valid = False
                elif ((r < 0) or (r >= len(self._grid))):
                    valid = False
                elif ((k < 0) or (k >= len(self._grid[0]))):
                    valid = False

                if valid:
                    adjc.append([r, k])
        return adjc


def main():
    file = "11e.in"

    g = Grid(file)
    g.simulateFlashing(100)

if __name__ == "__main__":
    main()