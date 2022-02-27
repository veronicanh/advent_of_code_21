# Løsninga funke, men e laangt ifra effektiv
# Okei fant ut av det, median for del 1, nesten avg for del 2 (dvs. +-1)

from collections import defaultdict

def absDiff(a, b):
    diff = a - b
    if diff < 0:
        diff = diff * (-1)
    return diff

def proportionalFuel(prop, dist):
    if dist not in prop:
        for i in range(max(prop.keys()), dist):
            prop[i + 1] = prop[i] + i + 1
    return prop[dist]

def main():
    file = "7.in"
    nums = [int(x) for x in open(file).readline().strip().split(",")]
    prop = {0:0}

    print("Avg:", avg(nums))

    distance = {}
    for i in range(max(nums)):
        distance[i] = 0

    for n in nums:
        for i in distance:
            distance[i] += proportionalFuel(prop, absDiff(n, i))

    minFuel = float("inf")
    placement = 0
    for p in distance:
        if distance[p] < minFuel:
            minFuel = distance[p]
            placement = p

    print("Placement:", placement, ", fuel used:", minFuel)
    print(min(distance.values()))



def avg(array, start = 0, stop = None):
    if (stop == None):
        stop = len(array)

    tot = 0
    for i in range(start, stop):
        tot += array[i]
    return tot / stop - start


if __name__ == "__main__":
    main()