import InputReader


class keypad:
    def __init__(self):
        self.pad = [['1', '2', '3'],
                    ['4', '5', '6'],
                    ['7', '8', '9']]
        self.padB = [['', '', '1', '', ''],
                     ['', '2', '3', '4', ''],
                     ['5', '6', '7', '8', '9'],
                     ['', 'A', 'B', 'C', ''],
                     ['', '', 'D', '', '']]
        self.code = ""
        self.x = 1
        self.y = 1

    def findKey(self, inputString):
        for char in inputString:
            if char is 'L' and self.x > 0:
                self.x -= 1
            elif char is 'R' and self.x < 2:
                self.x += 1
            elif char is 'U' and self.y > 0:
                self.y -= 1
            elif char is 'D' and self.y < 2:
                self.y += 1
        self.code += self.pad[self.y][self.x]


class keypadB:
    def __init__(self):
        self.pad = [['', '', '1', '', ''],
                    ['', '2', '3', '4', ''],
                    ['5', '6', '7', '8', '9'],
                    ['', 'A', 'B', 'C', ''],
                    ['', '', 'D', '', '']]
        self.code = ""

        self.x = 0
        self.y = 2

    def findKey(self, inputString):
        for char in inputString:
            tempx = self.x
            tempy = self.y
            if char is 'L' and tempx > 0:
                tempx -= 1
            elif char is 'R' and tempx < 4:
                tempx += 1
            elif char is 'U' and tempy > 0:
                tempy -= 1
            elif char is 'D' and tempy < 4:
                tempy += 1

            # if new key is not a valid key, reject it and stay on last key
            if not self.pad[tempy][tempx] is '':
                self.x = tempx
                self.y = tempy
        self.code += self.pad[self.y][self.x]


def run():
    data = InputReader.read("Inputs/2.txt")
    pad = keypad()
    padb = keypadB()
    for line in data:
        pad.findKey(line)
        padb.findKey(line)
    print("Code for keypad: {0}".format(pad.code))
    print("Code for keypad b: {0}".format(padb.code))


if __name__ == "__main__":
    run()
