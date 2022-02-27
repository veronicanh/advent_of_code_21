class SevenSegmentDisplay:
    def __init__(self):
        self._codes = {}

        self._digitToCode = []
        for i in range(10):
            self._digitToCode.append("-")

    def configure(self, signals):
        for s in sorted(signals, key=(lambda x: len(x))):
            if (len(s) == 2):
                self._encode(s, 1)
            elif (len(s) == 3):
                self._encode(s, 7)
            elif (len(s) == 4):
                self._encode(s, 4)
            elif (len(s) == 7):
                self._encode(s, 8)

            # Gjelder 2, 3 og 5
            elif (len(s) == 5):
                if (self._missingSegments(1, s) == 0):
                    self._encode(s, 3)
                elif (self._missingSegments(4, s) == 2):
                    self._encode(s, 2)
                elif (self._missingSegments(4, s) == 1):
                    self._encode(s, 5)

            # Gjelder 0, 6 og 9
            elif (len(s) == 6):
                if (self._missingSegments(1, s) == 1):
                    self._encode(s, 6)
                elif (self._missingSegments(4, s) == 1):
                    self._encode(s, 0)
                elif (self._missingSegments(4, s) == 0):
                    self._encode(s, 9)

    def _encode(self, code, digit):
        code = self._standardizeCode(code)
        self._codes[code] = digit
        self._digitToCode[digit] = code

    def _standardizeCode(self, code):
        arr = [char for char in code]
        arr.sort()
        code = ""
        for c in arr:
            code += c
        return code

    def _missingSegments(self, overlay, code):
        code = self._standardizeCode(code)
        cnt = 0
        for char in self._digitToCode[overlay]:
            if char not in code:
                cnt += 1
        return cnt

    def show(self, digits):
        result = ""
        for d in digits:
            result += str(self._codes[self._standardizeCode(d)])
        return int(result)



def decodeDisplay(signals, digits):
    display = SevenSegmentDisplay()
    display.configure(signals)
    return display.show(digits)


def main():
    fil = "8.in"

    cnt = 0
    for line in open(fil):
        line = line.strip().split(" | ")
        unique_signal_patterns = line[0].split(" ") #Combinations of signal LINES
        four_digit_output_value = line[1].split(" ")
        cnt += decodeDisplay(unique_signal_patterns, four_digit_output_value)
    print(cnt)

if __name__ == "__main__":
    main()

"""
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
"""