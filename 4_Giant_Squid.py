class Board:
    def __init__(self):
        self._board = []
        self._won = False

    def addRow(self, row):
        self._board.append(row)

    def haveWon(self):
        return self._won

    # Returns winnings-status
    def mark(self, x):
        for row in range(0, len(self._board)):
            for col in range(0, len(self._board[row])):
                num = self._board[row][col]

                if (num == x):
                    self._board[row][col] = "x"

                    self._won = self.checkIfWon(row, col)
                    return self._won
        return False

    def checkIfWon(self, row, col):
        return self.checkRow(row) or self.checkCol(col)

    def checkRow(self, row):
        for num in self._board[row]:
            if (num != "x"):
                return False
        return True

    def checkCol(self, col):
        for row in self._board:
            if (row[col] != "x"):
                return False
        return True

    def calculateSum(self, winningNum):
        unmarked = 0

        for row in self._board:
            for num in row:
                if (num != "x"):
                    unmarked += int(num)

        return unmarked * int(winningNum)

    def __str__(self):
        str = " B  I  N  G  O\n"
        for row in self._board:
            for num in row:
                if (len(num) == 1):
                    str += " "
                str += num + " "
            str += "\n"
        return str

def makeBoards(file):
    line = file.readline()
    boards = []
    board = None

    while line:
        if (line.strip() == ""):
            board = Board()
            boards.append(board)
        else:
            board.addRow(line.strip().split())
        line = file.readline()

    return boards


def playGame(nums, boards):
    for n in nums:
        for b in boards:
            if not b.haveWon():
                hasWon = b.mark(n)
                if hasWon:
                    print("WON! Score:", b.calculateSum(n))

def main():
    file = open("4.in")

    numbers = file.readline().strip().split(",")
    boards = makeBoards(file)

    playGame(numbers, boards)

if __name__ == "__main__":
    main()