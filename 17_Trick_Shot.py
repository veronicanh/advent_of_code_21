def xVelocityRange(targetLimits):
    minVelocity = xMinVelocity(targetLimits[0]) # Must reach xMin for target
    maxVelocity = targetLimits[1]               # Everything bigger will overshoot the target
    return [minVelocity, maxVelocity]

# Finds the minimun x-velocity required to reach the target-area
def xMinVelocity(targetStartX):
    minVel = 0
    reaches = 0
    while reaches < targetStartX:
        minVel += 1
        reaches = (minVel * (minVel + 1)) / 2 # Sum of natural numbers, 1 + 2 + 3 + ... + N
    return minVel


def yVelocityRange(targetLimits):
    minVelocity = targetLimits[0]          # Everything smaller goes under target
    maxVelocity = abs(targetLimits[0]) - 1 # Everything bigger overshoot the target, because the first negative value it has is negative(velocity + 1)
    return [minVelocity, maxVelocity]

# Finds the minimun x-velocity required to reach the target-area
def highestReachedPoint(velocity):
    yPos = 0
    while (velocity > 0):
        yPos += velocity
        velocity -= 1
    return yPos


def findTargetVelocities(xRange, yRange, xTarget, yTarget):
    valid = []

    for xVel in range(xRange[0], xRange[1] + 1):
        for yVel in range(yRange[0], yRange[1] + 1):
            if (reachesTarget(xVel, yVel, xTarget, yTarget)):
                valid.append((xVel, yVel))

    return valid

def reachesTarget(xVel, yVel, xTarget, yTarget):
    xPos = 0
    yPos = 0

    while ((xPos <= xTarget[1]) and (yPos >= yTarget[0])):
        xPos += xVel
        yPos += yVel

        if (xVel > 0):
            xVel -= 1
        yVel -= 1

        if ((xTarget[0] <= xPos <= xTarget[1]) and
            (yTarget[0] <= yPos <= yTarget[1])):
            return True

    return False


def readFile(file):
    bits = open(file).readline().strip().replace("target area: ", "").split(", ")
    x = [int(x) for x in bits[0].replace("x=", "").split("..")]
    y = [int(x) for x in bits[1].replace("y=", "").split("..")]
    return x, y

def main():
    file = "17.in"
    xTarget, yTarget = readFile(file)

    xRange = xVelocityRange(xTarget)
    yRange = yVelocityRange(yTarget)
    print("Part 1:", highestReachedPoint(yRange[1]))

    allVelocities = findTargetVelocities(xRange, yRange, xTarget, yTarget)
    print("Part 2:", len(allVelocities))

if __name__ == "__main__":
    main()
