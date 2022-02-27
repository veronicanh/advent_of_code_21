def readNumbers(file):
    nums = []
    for line in open(file):
        nums.append(int(line))
    return nums


def solve(nums):
    increases = 0

    prev = 0
    this = 0

    for i in range(0, (len(nums) - 2)):
        prev = this

        this = 0
        for j in range(i, i+3):
            this += nums[j]

        if (i != 0):
            if (prev < this):
                increases += 1
    
    return increases



def main():
    nums = readNumbers("1-1.in")
    answ =solve(nums)
    print(answ)

if __name__ == "__main__":
    main()
