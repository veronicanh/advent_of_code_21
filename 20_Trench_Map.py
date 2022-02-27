class Image:
    def __init__(self, infinteChar="."):
        self._grid = []
        self._infiniteChar = infinteChar

    def __str__(self):
        prettyStr = ""
        for row in self._grid:
            for pixel in row:
                prettyStr += str(pixel) + ""
            prettyStr += "\n"
        return prettyStr

    def addPixelRow(self, row):
        self._grid.append(row)

    def enhanced(self, enhancement):
        newInfiniteChar = enhancement[self._adcjCodeToBinary(self._infiniteChar * 9)]
        newImage = Image(newInfiniteChar)
        for r in range(-2, (2 + len(self._grid))):
            pixels = []
            for c in range(-2, (2 + len(self._grid[0]))):
                code = self._findAdjacent(r, c)
                index = self._adcjCodeToBinary(code)
                pixels.append(enhancement[index])
            newImage.addPixelRow(pixels)
        return newImage

    # 3x3 grid arount a given point, if along an edge: infinite grid of "."
    def _findAdjacent(self, rad, col):
        adjc = ""
        for rDiff in range(-1, 2):
            for kDiff in range(-1, 2):
                r = rad + rDiff
                c = col + kDiff

                if ((r < 0) or (r >= len(self._grid))):
                    adjc += self._infiniteChar
                elif ((c < 0) or (c >= len(self._grid[0]))):
                    adjc += self._infiniteChar
                else:
                    adjc += self._grid[r][c]
        return adjc

    def _adcjCodeToBinary(self, code):
        code = code.replace(".", "0")
        code = code.replace("#", "1")
        return int(code, base=2)

    def countLitPixels(self):
        cnt = 0
        for row in self._grid:
            for pixel in row:
                if (pixel == "#"):
                    cnt += 1
        return cnt

def readFile(file):
    f = open(file)
    enhancementAlgorithm = f.readline()
    f.readline()

    image = Image()
    for line in f.readlines():
        image.addPixelRow([x for x in line.strip()])

    return image, enhancementAlgorithm


def main():
    file = "20.in"
    image, enhancement = readFile(file)
    print(image)

    for i in range(50):
        image = Image.enhanced(image, enhancement)

        if (i == 1):
            print("Part 1:", image.countLitPixels())
    
    print("Part 2:", image.countLitPixels())
    


if __name__ == "__main__":
    main()