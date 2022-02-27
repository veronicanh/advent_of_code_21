class Submarine:
    def __init__(self):
        self._horizontal = 0
        self._depth = 0
        self._aim = 0

    def forward(self, x):
        self._horizontal += x
        self._depth += (x * self._aim)

    def down(self, x):
        self._aim += x

    def up(self, x):
        self._aim -= x

    def printInfo(self):
        print("Horizontal position:", self._horizontal)
        print("Depth:", self._depth)
        print("Answer:", self._horizontal * self._depth)




def main():
    file = "2.in"
    s = Submarine()

    for line in open(file):
        cmd, x = line.split()
        x = int(x)

        if (cmd == "forward"):
            s.forward(x)
        elif (cmd == "down"):
            s.down(x)
        elif (cmd == "up"):
            s.up(x)
        else:
            print("Ugyldig kommando:", cmd)

    s.printInfo()


if __name__ == "__main__":
    main()