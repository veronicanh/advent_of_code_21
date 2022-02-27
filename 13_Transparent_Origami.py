class Grid:
    def __init__(self, file):
        self._dots = set()
        self._folds = []
        # self._grid = []

        self._readFile(file)

    def _readFile(self, file):
        f = open(file)

        line = f.readline()
        while line != "\n":
            dot = tuple([int(x) for x in line.strip().split(",")])
            self._dots.add(dot)
            line = f.readline()

        line = f.readline()
        while line != "":
            fold = line.replace("fold along", "").strip().split("=")

            axis = fold[0]
            pos = int(fold[1])
            if (axis == "x"):
                self._folds.append([pos, None])
            else:
                self._folds.append([None, pos])

            line = f.readline()

    def fold(self):
        for fold in self._folds:

            newDots = set()
            for dot in self._dots:
                newDots.add(self._foldDot(dot, fold))
            self._dots = newDots

            if (fold == self._folds[0]):
                print("Part 1:", len(self._dots))
        print("Part 2:")
        self.displayDots()


    def _foldDot(self, dot, fold):
        newDot = [x for x in dot]
        for axis in range(len(fold)):
            if (fold[axis] == None):
                continue

            if (dot[axis] > fold[axis]):
                new = fold[axis] - (dot[axis] - fold[axis])
                newDot[axis] = new

        return tuple(newDot)

    def displayDots(self):
        grid = [[]]
        for dot in self._dots:
            while dot[1] >= len(grid):
                grid.append([" " for i in range(len(grid[0]))])

            while dot[0] >= len(grid[0]):
                for row in grid:
                    row.append(" ")

            grid[dot[1]][dot[0]] = "█"

        for row in grid:
            for char in row:
                print(char, end="")
            print()


def main():
    file = "13.in"
    g = Grid(file)
    g.fold()


if __name__ == "__main__":
    main()