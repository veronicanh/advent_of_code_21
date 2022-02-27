def matchingChar(char, opening, closing):
    for i in range(len(opening)):
        if char == opening[i]:
            return closing[i]

def decodeLine(line, opening, closing):
    stack = []

    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            expected = matchingChar(stack.pop(), opening, closing)
            if (char != expected):
                print("Expected " + expected + ", but found " + char + " instead.")
                stack = []
                break
                return char

    add = ""
    while len(stack) != 0:
        add += matchingChar(stack.pop(), opening, closing)

    if len(add) != 0:
        print("Incomplete line - Complete by adding", add)
    return add


def main():
    file = "10.in"
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]
    points = {")":1, "]":2, "}":3, ">":4, None:0}

    allScores = []

    for line in open(file):
        error = decodeLine(line.strip(), opening, closing)
        if error:
            score = 0
            for char in error:
                score = score * 5
                score += points[char]
            allScores.append(score)

    allScores.sort()
    print("Score:", allScores[int(len(allScores)/2)])



if __name__ == "__main__":
    main()