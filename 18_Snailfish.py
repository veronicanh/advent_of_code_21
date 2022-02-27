import math

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = 0
        self.parent = None

        if (self.isInternal()):
            left.setParent(self)
            right.setParent(self)

    def __str__(self) -> str:
        if (self.data == None):
            return "[" + str(self.left) + "," + str(self.right) + "]"
        else:
            return str(self.data)

    def __add__(self, other):
        return self.addNode(other)

    def deepCopy(self):
        if (self.isNumber()):
            return Node(self.data)
        else:
            return Node(self.data, self.left.deepCopy(), self.right.deepCopy())

    # Må kalles på en rotnode
    def addNode(self, other):
        n = Node(None, self.deepCopy(), other.deepCopy())
        #print("Reducing:" + str(self.getRoot()))
        n.reduce()
        return n

    def setParent(self, parent):
        self.parent = parent
        self.updateDepth()

    def updateDepth(self):
        self.depth = self.parent.depth + 1
        if (self.isInternal()):
            self.left.updateDepth()
            self.right.updateDepth()

    def isNumber(self):
        return self.data != None

    def isInternal(self):
        return (self.left != None) and (self.right != None)

    def getRoot(self):
        if (self.parent == None):
            return self
        return self.parent.getRoot()

    def _addData(self, value):
        self.data += value


    def reduce(self):
        changes = -1
        while changes != 0:
            #print(changes)
            changes = -1
            while changes != 0:
                changes = self.reduceIter(doExplo=True)
                #print("changes", changes)

            #print("changes1", changes)


            if (changes == 0):
                changes = self.reduceIter(doExplo=False)

            #print("changes222", changes)


        return changes

    def reduceIter(self, doExplo):
        changes = 0
        explo = self.shouldExplode()
        split = self.shouldSplit()

        if (explo and doExplo):
            self._explode()
            #print("exploded:" + str(self.getRoot()))
            changes += 1

            #if (l != None and l.shouldSplit()):
            #print("EXPLODED; SJEKKER FRA", l.data)
            #    changes += l.reduceIter(False)

        elif (split and (not doExplo)):
            self._split()
            #print("splitted:" + str(self.getRoot()))
            return 1

        #if (split and (self.shouldExplode())):
        #    changes += self.reduceIter(True)


        if (self.isInternal()):
            changes += self.left.reduceIter(doExplo)
            if ((not doExplo) and changes != 0):
                return changes
            changes += self.right.reduceIter(doExplo)

        return changes




    def reduceOld(self):
        if (self.isInternal()):
            if (self.depth >= 4):
                #print(self, end="")
                self._explode()
                print("exploded:" + str(self.getRoot()))
                self.reduce()
                return True
            else:
                l = self.left.reduce()
                if (l):
                    return l
                return self.right.reduce()
        else:
            if (self.data >= 10):
                #print(self.data, end="   ")
                self._split()
                print("splitted:" + str(self.getRoot()))
                self.reduce()
                return True
        return False

    def shouldExplode(self):
        return self.isInternal() and (self.depth >= 4)

    def shouldSplit(self):
        return self.isNumber() and (self.data >= 10)

    def _split(self):
        self.left = Node(math.floor(self.data / 2))
        self.right = Node(math.ceil(self.data / 2))
        self.left.setParent(self)
        self.right.setParent(self)

        self.data = None

    def _explode(self):
        root = self.getRoot()

        left = root._addToSide(self, self.left.data, Node.fromLeft)
        root._addToSide(self, self.right.data, Node.fromRight)

        self.data = 0
        self.left = None
        self.right = None

        return left

    def _addToSide(self, node, data, searchFrom):
        neighbor = self.searchFromSide(node, searchFrom, [])
        if (neighbor != None):
            neighbor._addData(data)
        return neighbor

    def searchFromSide(self, node, searchFrom, visited):
        if (self == node):
            if (len(visited) == 0):
                return None
            return visited.pop()
        elif (self.isNumber()):
            visited.append(self)
            return False

        return searchFrom(self, node, visited)

    def fromRight(self, node, visited):
        r = self.right.searchFromSide(node, Node.fromRight, visited)
        if (r != False):
            return r
        return self.left.searchFromSide(node, Node.fromRight, visited)

    def fromLeft(self, node, visited):
        r = self.left.searchFromSide(node, Node.fromLeft, visited)
        if (r != False):
            return r
        return self.right.searchFromSide(node, Node.fromLeft, visited)


    def magnitude(self):
        if (self.isNumber()):
            return int(self.data)
        return (3 * self.left.magnitude()) + (2 * self.right.magnitude())


def decodeNumber(line):
    if (line[0] != "["):
        return Node(int(line))

    indent = 0
    left = None
    temp = ""
    for char in line:
        if (char == "["):
            indent += 1
        elif (char == "]"):
            indent -= 1

        if ((indent == 1) and (char == ",")):
            left = temp[1:]
            temp = ""
        elif (indent != 0):
            temp += char
    right = temp

    return Node(None, decodeNumber(left), decodeNumber(right))


def main():
    print(
        "---------------------------------------------------------------------------------------------------"
    )
    file = "18.in"
    numbers = []
    for line in open(file):
        if (line[0] != "#"):
            n = decodeNumber(line.strip())
            numbers.append(n)

    sum = numbers[0] + numbers[1]
    for i in range(2, len(numbers)):
        sum = sum + numbers[i]
    print("Result:", sum)
    print("Part 1:", sum.magnitude())

    biggest = 0
    for i in range(0, len(numbers)):
        for j in range((i + 1), len(numbers)):
            sum1 = numbers[i] + numbers[j]
            sum2 = numbers[j] + numbers[i]

            b = max(sum1.magnitude(), sum2.magnitude())
            biggest = max(biggest, sum1.magnitude(), sum2.magnitude())

    print("Part 2:", biggest)


if __name__ == "__main__":
    main()
