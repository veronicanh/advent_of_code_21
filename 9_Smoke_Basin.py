class Heightmap:
    def __init__(self, file):
        self._map = self._readFile(file)

    def _readFile(self, file):
        map = []
        for line in open(file):
            map.append([int(x) for x in line.strip()])
        return map

    def findLowPoints(self):
        riskLevel = 0

        for rad in range(len(self._map)):
            for kol in range(len(self._map[rad])):
                lowest = min(self._findAdjacent(rad, kol))
                if self._map[rad][kol] < lowest:
                    riskLevel += 1 + self._map[rad][kol]

        return riskLevel

    def findBasins(self):
        basinSizes = []

        for rad in range(len(self._map)):
            for kol in range(len(self._map[rad])):
                if (not (self._map[rad][kol] in [" ", 9])):
                    basinSizes.append(self._explore(rad, kol))

        basinSizes.sort()
        return basinSizes[-1] * basinSizes[-2] * basinSizes[-3]

    def _explore(self, rad, kol):
        if (self._map[rad][kol] in [" ", 9]):
            return 0

        size = 1
        self._map[rad][kol] = " "

        for diffs in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            r = rad + diffs[0]
            k = kol + diffs[1]

            if (not ((r < 0) or (r >= len(self._map)) or
                     (k < 0) or (k >= len(self._map[0])))):
                size += self._explore(r, k)

        return size

    def _findAdjacent(self, rad, kol):
        adjc = []

        for diffs in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            r = rad + diffs[0]
            k = kol + diffs[1]

            if (not ((r < 0) or (r >= len(self._map)) or
                     (k < 0) or (k >= len(self._map[0])))):
                adjc.append(self._map[r][k])

        return adjc


def main():
    file = "9.in"

    m = Heightmap(file)
    print("Risk:", m.findLowPoints())
    print("Biggest basins:", m.findBasins())


if __name__ == "__main__":
    main()