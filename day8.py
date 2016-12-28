import InputReader
import numpy


class codeDisplay:
    def __init__(self, height, width):
        self.display = numpy.zeros((height, width))  # (Y,X)

    def readInput(self, line):
        if "rect" in line:
            self.turnOn(line)
        elif "column" in line:
            self.rotateColumn(line)
        elif "row" in line:
            self.rotateRow(line)
        else:
            print("Unexpected input: \"{0}\"".format(line))

    def turnOn(self, line):
        split = line.split('x')
        width = int(split[0].split(' ')[1])
        height = int(split[1])
        self.display[0:height, 0:width] = 1

    def rotateColumn(self, line):
        split = line.split("=")[1].split("by")
        column = int(split[0])
        ammount = int(split[1])
        self.display[:, column] = self.moveArray(self.display[:, column], ammount)

    def rotateRow(self, line):
        split = line.split("=")[1].split("by")
        row = int(split[0])
        ammount = int(split[1])
        self.display[row, :] = self.moveArray(self.display[row, :], ammount)

    def moveArray(self, array, ammount):
        movedArray = numpy.zeros(len(array))
        for index in range(len(array)):
            movedArray[(index + ammount) % len(array)] = array[index]
        return movedArray

    def printLetters(self):
        """Converts the numeric matrix to a char matrix to make the characters more visible"""
        charDisplay = numpy.empty([6, 50], dtype=numpy.str_)
        for row in range(numpy.size(self.display, axis=1)):
            for column in range(len(self.display)):
                if self.display[column, row] == 0:
                    charDisplay[column, row] = " "
                else:
                    charDisplay[column, row] = '#'

        for letter in range(numpy.size(self.display, axis=1) / 5):
            print(charDisplay[:, letter * 5:letter * 5 + 5])
            print ""


def run():
    data = InputReader.read("Inputs/8.txt")
    display = codeDisplay(6, 50)
    for line in data:
        display.readInput(line)

    print(numpy.sum(display.display))
    # display.printLetters()  # part 2 of assignment


if __name__ == "__main__":
    run()
