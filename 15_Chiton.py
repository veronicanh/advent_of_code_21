from collections import defaultdict
from heapq import heappush, heappop


class Grid:
    def __init__(self, file):
        self._grid = self._readFile(file)

        self._maxRow = len(self._grid)
        self._maxCol = len(self._grid[0])

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
            map.append([int(x) for x in line.strip()])
        return map

    def _findAdjacent(self, node):
        rad = node[0]
        kol = node[1]

        adjc = []
        for diff in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            r = rad + diff[0]
            k = kol + diff[1]

            if not ((r < 0) or (k < 0) or (r >= self._maxRow) or (k >= self._maxCol)):
                adjc.append((r, k))

        return adjc

    # Dijkstra
    def shortestPath(self):
        start = (0,0)
        end = (self._maxRow - 1 , self._maxCol - 1)
        print("\n")
        print("Part 1:", self._dijkstra(start, end))

        self._maxRow = self._maxRow * 5
        self._maxCol = self._maxCol * 5
        end = (self._maxRow - 1 , self._maxCol - 1)
        print("Part 2:", self._dijkstra(start, end))

    def _dijkstra(self, start, end):
        distance = defaultdict(lambda: float('inf'))
        path = defaultdict(lambda: None)

        distance[start] = 0
        Q = [(0, start)]

        while Q:
            cost, v = heappop(Q)

            for nabo in self._findAdjacent(v):
                c = cost + self._findCost(nabo[0], nabo[1])

                if (c < distance[nabo]):
                    distance[nabo] = c
                    heappush(Q, (c, nabo))
                    path[nabo] = v

        self._printDistances(distance)
        #self._printPaths(path, end)
        return distance[end]

    def _findCost(self, r, k):
        #wrapper rundt siden kartet gjentas i begge retninger
        row = r % len(self._grid)
        col = k % len(self._grid[0])

        utvRow = r // len(self._grid)
        utvCol = k // len(self._grid[0])
        antUtvidelser = utvRow + utvCol

        # cost looper gjennom [1 2 ... 9 1 2] for hver utvidelse
        nCost = (self._grid[row][col] + antUtvidelser) % 9
        if (nCost == 0):
            nCost = 9

        return nCost

    def _printDistances(self, distance):
        s = []
        for line in str(self).split("\n"):
            for i in range(5):
                row = []
                for i in range(5):
                    for char in line:
                        row.append(char)
                s.append(row)

        for r in range(len(s)):
            if (r % len(self._grid) == 0):
                print()
            for k in range(len(s[r])):
                if (k % len(self._grid[0]) == 0) and k != 0:
                    print(" ,", end="")
                
                dd = str(distance[(r,k)])
                while len(dd) < 3:
                    dd = " " + dd
                print(dd, end=",")

            print()

    def _printPaths(self, path, end):
        s = []
        for line in str(self).split("\n"):
            for i in range(5):
                row = []
                for i in range(5):
                    for char in line:
                        row.append(char)
                s.append(row)

        hm = end
        while hm != None:
            s[hm[0]][hm[1]] = "*"
            hm = path[hm]

        for r in range(len(s)):
            if (r % len(self._grid) == 0):
                print()
            for k in range(len(s[r])):
                if (k % len(self._grid[0]) == 0):
                    print(" ", end="")

                c = s[r][k]
                if (c == "*"):
                    print("{" + str(self._findCost(r, k)), end="}")
                else:
                    print("", self._findCost(r, k), end=" ")
                    print("", end="")
            print()

def main():
    file = "15e.in"

    g = Grid(file)
    #print(g)
    g.shortestPath()


if __name__ == "__main__":
    main()


# 993

# FEIL: 2918