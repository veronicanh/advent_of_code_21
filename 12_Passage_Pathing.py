from collections import defaultdict
from typing import Tuple

class CaveSystem:
    def __init__(self, file):
        self._start = "start"
        self._end = "end"

        self._caveSystem = defaultdict(list)
        self._readFile(file)

    def _readFile(self, file):
        for line in open(file):
            caves = line.strip().split("-")
            self._caveSystem[caves[0]].append(caves[1])
            self._caveSystem[caves[1]].append(caves[0])

    def findAllPaths(self):
        visited = defaultdict(lambda: 0)
        validStep = (lambda cave, visited: not(cave.islower() and visited[cave] >= 1))
        print("Part 1:", self._dfs(self._start, visited, validStep))

        visited = defaultdict(lambda: 0)
        validStep = (lambda cave, visited: cave != self._start)
        print("Part 2:", self._dfs(self._start, visited, validStep))


    def _dfs(self, cave, visited, validStep):
        paths = 0
        visited[cave] += 1

        # Maximum one small cave can be visited two times in a path
        if (cave.islower() and visited[cave] == 2):
            validStep = (lambda cave, visited: not(cave.islower() and visited[cave] >= 1))

        for n in self._caveSystem[cave]:
            if (n == self._end):
                paths += 1
            elif (validStep(n, visited)):
                paths += self._dfs(n, visited, validStep)

        visited[cave] -= 1
        return paths



def main():
    file = "12.in"
    c = CaveSystem(file)
    c.findAllPaths()

if __name__ == "__main__":
    main()