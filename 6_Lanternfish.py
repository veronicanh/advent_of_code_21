def main():
    daysGrowing = 256

    reproductionDays = 7 - 1
    growingDays = 2

    fishies = []
    for i in range(reproductionDays + growingDays + 1):
        fishies.append(0)

    for line in open("6e.in"):
        for fish in line.strip().split(","):
            fishies[int(fish)] += 1

    print("Initial state:", fishies)

    for day in range(daysGrowing):
        reproductiveFishies = fishies[0]

        for i in range(1, len(fishies)):
            fishies[i-1] += fishies[i]
            fishies[i] = 0

        fishies[0] -= reproductiveFishies
        # Reproduction
        fishies[reproductionDays] += reproductiveFishies
        fishies[reproductionDays + growingDays] += reproductiveFishies

        if (day % 20 == 19) or (day < 20):
            print("After", (day + 1), "days:", sum(fishies), fishies)

    print("Total fish after", (day + 1), "days:", sum(fishies))


if __name__ == "__main__":
    main()


"""
for i in range(len(fishies)):
    if (fishies[i] == 0):
        fishies[i] = reproductionDays
        fishies.append(reproductionDays + growingDays)
    else:
        fishies[i] -= 1
"""