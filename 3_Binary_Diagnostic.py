def readInput(file):
    a = []
    for line in open(file):
        l = []
        for tall in line.strip():
            l.append(int(tall))
        a.append(l)
    return a

def mostCommonBit(numbers, bit_pos):
    num0 = 0
    num1 = 0

    for n in numbers:
        if (n[bit_pos] == 0):
            num0 += 1
        else:
            num1 += 1

    if (num0 > num1):
        return 0
    elif (num0 < num1):
        return 1
    else:
        return 1


def findGammaRate(array):
    result = []

    for bit_pos in range(len(array[0])):
        result.append(mostCommonBit(array, bit_pos))

    return result

def invert_binary(num):
    result = []

    for t in num:
        if (t == 0):
            result.append(1)
        else:
            result.append(0)

    return result


def findOxygen(array):
    result = array.copy()
    bit_pos = 0

    while (len(result) != 1):
        required_bit = mostCommonBit(result, bit_pos)

        this = []
        for t in result:
            if (t[bit_pos] == required_bit):
                this.append(t)

        bit_pos += 1
        result = this

    return result[0]

def findCO2(array):
    result = array.copy()
    bit_pos = 0

    while (len(result) != 1):
        required_bit = mostCommonBit(result, bit_pos)

        this = []
        for t in result:
            if (t[bit_pos] != required_bit):
                this.append(t)

        bit_pos += 1
        result = this

    return result[0]


def decimal(binary_array):
    copy = binary_array.copy()
    copy.reverse()
    result = 0

    for i in range(0, len(copy)):
        result += copy[i] * (2 ** i)

    return result


def main():
    input = readInput("3.in")

    gamma_rate = findGammaRate(input)
    epsilon_rate = invert_binary(gamma_rate)

    power_consumption = decimal(gamma_rate) * decimal(epsilon_rate)
    print("Power consumption:", power_consumption)


    oxygen_generator = findOxygen(input)
    CO2_scrubber = findCO2(input)

    life_support = decimal(oxygen_generator) * decimal(CO2_scrubber)
    print("Life support:", life_support)



if __name__ == "__main__":
    main()