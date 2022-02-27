from functools import reduce

class Packet:
    def __init__(self, binaryCode):
        self._bitsRead = 0

        self._literal = False
        self._value = None
        self._subPackets = []

        self._binaryCode = binaryCode
        self._version = self.toDecimal(self.readBits(3))
        self._typeID = self.toDecimal(self.readBits(3))

        self._decode()

    def __str__(self):
        return "Packet version_" + str(self._version) + " typeID_" + str(self._typeID)

    def getValue(self):
        return self._value

    def getBitsRead(self):
        return self._bitsRead

    # Takes in a string/char-array of a number in binary, resturns number as int in decimal
    def toDecimal(self, binary=None):
        if (binary == None):
            binary = self._binaryCode

        binaryInts = [int(bit) for bit in binary]
        number = 0
        for i in range(len(binaryInts)):
            bit = binaryInts.pop()
            number += bit * (2**i)
        return number


    # Manipulate binary packet(/code)
    #
    def readNextBit(self, packet=None):
        if (packet == None):
            packet = self._binaryCode
        self._bitsRead += 1
        return packet.pop(0)

    def readBits(self, num, packet=None):
        if (packet == None):
            packet = self._binaryCode
        self._bitsRead += num
        return [packet.pop(0) for i in range(num)]


    # Interpreting the binary code
    #
    def _decode(self):
        # Literal value packets, encode a single binary number
        if (self._typeID == 4):
            self._value = self._evaluateLiteralValue()
            return

        # Operators
        self._subPackets = self._decodeOperatorPackets()
        self._value = self._evaluateOperator()

    def _evaluateLiteralValue(self):
        self._literal = True
        binary = []

        prefix = None
        while (prefix != "0"):
            prefix = self.readNextBit()
            binary += self.readBits(4)
        return self.toDecimal(binary)

    # Recursive method, because operators consist of one or more sub-packets
    def _decodeOperatorPackets(self):
        packets = []
        lengthTypeID = self.readNextBit()

        if (lengthTypeID == "0"):
            subpacketsLength = self.toDecimal(self.readBits(15))
            stopAtBit = self._bitsRead + subpacketsLength
            while (self._bitsRead < stopAtBit):
                packets.append(self._readSubPacket())
        elif (lengthTypeID == "1"):
            subpacketsCount = self.toDecimal(self.readBits(11))
            for i in range(subpacketsCount):
                packets.append(self._readSubPacket())

        return packets

    def _readSubPacket(self):
        p = Packet(self._binaryCode)
        self._bitsRead += p.getBitsRead()
        return p


    def _evaluateOperator(self):
        # sum
        if (self._typeID == 0):
            return sum(p.getValue() for p in self._subPackets)
        # product
        elif (self._typeID == 1):
            return reduce((lambda x, y: x * y), map(Packet.getValue, self._subPackets))

        # min-value
        elif (self._typeID == 2):
            return min(p.getValue() for p in self._subPackets)
        # max-value
        elif (self._typeID == 3):
            return max(p.getValue() for p in self._subPackets)

        # greater than
        elif (self._typeID == 5):
            return int(self._subPackets[0].getValue() > self._subPackets[1].getValue())
        # less than
        elif (self._typeID == 6):
            return int(self._subPackets[0].getValue() < self._subPackets[1].getValue())
        # equal to
        elif (self._typeID == 7):
            return int(self._subPackets[0].getValue() == self._subPackets[1].getValue())



    def _product(self):
        prod = 1
        for p in self._subPackets:
            prod = prod * p.getValue()
        return prod


    # Used for puzzle part 1
    def getSumVersion(self):
        return self._version + sum([p.getSumVersion() for p in self._subPackets])

#VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
#-------------------------------------------------
#0011100000000000011011110100010100101001000100100 0000000

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# Takes in a string/char-array of hexadesimal code, resturns char-array convertet to binary
def toBinary(hexaCode):
    binaryCode = []
    for char in hexaCode:
        binaryCode += [c for c in HEXADECIMAL[char]]
    return binaryCode

def test():
    file = "16e.in"
    for line in open(file):
        if (line[0] != "#"):
            print("\n-=-=( " + line.strip() + " )=-=-=-=-=-=")
            p = Packet(toBinary(line.strip()))
            print("Part 1:", p.getSumVersion())
            print("Part 2:", p.getValue())

def main():
    defineHexadecimal("hexadecimal.txt")

    #test()
    #print()

    print("\n-=-=( 16.in )=-=-=-=-=-=")
    file = "16.in"
    p = Packet(toBinary(open(file).readline().strip()))
    print("Part 1:", p.getSumVersion())
    print("Part 2:", p.getValue())

# Defines hexadecimal constant
def defineHexadecimal(file):
    global HEXADECIMAL
    HEXADECIMAL = {}
    for line in open(file):
        l = line.strip().split(" = ")
        HEXADECIMAL[l[0]] = l[1]
    return HEXADECIMAL


if (__name__ == "__main__"):
    main()
