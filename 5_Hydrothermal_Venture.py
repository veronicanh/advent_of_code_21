class Grid:
    def __init__(self):
        self._grid = []
        self._x = 0
        self._y = 0

    def expand(self, x1, y1, x2, y2):
        if ((self._y <= y1) or (self._y <= y2)):
            self.expandGridY(max(y1, y2))

        if ((self._x <= x1) or (self._x <= x2)):
            self.expandGridX(max(x1, x2))

    def expandGridY(self, newY):
        for y in range(1 + newY - self._y):
            row = []
            for x in range(self._x):
                row.append(0)
            self._grid.append(row)
        self._y = newY + 1

    def expandGridX(self, newX):
        for row in self._grid:
            for x in range(1 + newX - self._x):
                row.append(0)
        self._x = newX + 1

    def drawLine(self, x1, y1, x2, y2):
        self.expand(x1, y1, x2, y2)

        xDiff = 0
        if (x1 < x2):
            xDiff = +1
        elif (x1 > x2):
            xDiff = -1
        else:
            xDiff = 0

        yDiff = 0
        if (y1 < y2):
            yDiff = +1
        elif (y1 > y2):
            yDiff = -1
        else:
            yDiff = 0

        #diagonal = not ((x1 == x2) or (y1 == y2))

        self._grid[y1][x1] += 1
        while not ((x1 == x2) and (y1 == y2)):
            x1 += xDiff
            y1 += yDiff
            self._grid[y1][x1] += 1

        """
        evt:
        
        diagonal = not ((x1 == x2) or (y1 == y2))
        if diagonal:
            pass
        else:
            for x in range(min(x1, x2), (max(x1, x2))):
                self._grid[y1][x] += 1
            for y in range(min(y1, y2), (max(y1, y2))):
                self._grid[y][x1] += 1
            self._grid[max(y1, y2)][max(x1, x2)] += 1
        """

    def countDangerous(self):
        cnt = 0
        for row in self._grid:
            for point in row:
                if (point >= 2):
                    cnt += 1
        return cnt

    def __str__(self):
        prettyStr = ""
        for row in self._grid:
            for point in row:
                if (point == 0):
                    prettyStr += "." + " "
                else:
                    prettyStr += str(point) + " "
            prettyStr += "\n"
        return prettyStr

def main():
    grid = Grid()

    for line in open("5.in"):
        line = line.strip().split(" -> ")
        line = line[0].split(",") + line[1].split(",")
        xy = [int(x) for x in line]

        grid.drawLine(xy[0], xy[1], xy[2], xy[3])

    if (grid._x < 15):
        print(grid)
    print("Dangerous points:", grid.countDangerous())

if __name__ == "__main__":
    main()
