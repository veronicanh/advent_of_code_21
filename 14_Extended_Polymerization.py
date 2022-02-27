from collections import defaultdict

def readFile(file):
    file = open(file)
    polymer = file.readline().strip() #[c for c in file.readline().strip()]

    insertions = defaultdict(lambda: False)
    line = file.readline()
    line = file.readline()
    while line:
        l = line.strip().split(" -> ")
        insertions[l[0]] = l[1]
        line = file.readline()

    return polymer, insertions

def makePairs(polymer):
    pairs = defaultdict(lambda: 0)
    for i in range(1, len(polymer)):
        t = polymer[i - 1] + polymer[i]
        pairs[t] += 1
    return pairs

def insert(iters, pairs, insertions):
    for iter in range(iters):
        neste = pairs.copy()

        for pair in pairs:
            insert = insertions[pair]

            if (insert):
                ant = pairs[pair]
                neste[pair] -= ant
                neste[pair[0] + insert] += ant
                neste[insert + pair[1]] += ant
        pairs = neste

    return pairs

def decode(pairs, start, end):
    freq = defaultdict(lambda: 0)

    freq[start] += 1/2
    freq[end] += 1/2
    for pair in pairs:
        for char in pair:
            freq[char] += (1 * pairs[pair]) / 2

    mostCommon = 0
    leastCommon = 999999999999999999999999999999999999999999
    for char in freq:
        freq[char] = int(freq[char])
        if (freq[char] > mostCommon):
            mostCommon = freq[char]
        if (freq[char] < leastCommon):
            leastCommon = freq[char]

    return (mostCommon - leastCommon)

def main():
    file = "14.in"

    polymer, insertions = readFile(file)

    pairs = makePairs(polymer)
    start = polymer[0]
    end = polymer[len(polymer) - 1]

    pairFreq = insert(10, pairs, insertions)
    print("Part 1:", decode(pairFreq, start, end))

    pairFreq = insert(40, pairs, insertions)
    print("Part 2:", decode(pairFreq, start, end))


if __name__ == "__main__":
    main()