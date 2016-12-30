import InputReader
import re


class Chip:
    def __init__(self, value, currentBot):
        self.value = value
        self.currentBot = currentBot


class Bot:
    def __init__(self, name, low, high, botList):
        self.name = name
        self.low = low
        self.high = high
        self.chips = []
        self.botlist = botList

    def giveChips(self):
        if self.chips[0].value < self.chips[1].value:
            self.botlist[self.low].recieveChip(self.chips[0])
            self.botlist[self.high].recieveChip(self.chips[1])
        else:
            self.botlist[self.low].recieveChip(self.chips[1])
            self.botlist[self.high].recieveChip(self.chips[0])
        self.chips = []

    def recieveChip(self, chip):
        chip.currentBot = self.name
        self.chips.append(chip)


class Output:
    def __init__(self, name):
        self.name = name
        self.chips = []

    def recieveChip(self, chip):
        chip.currentBot = self.name
        self.chips.append(chip)


def run():
    data = InputReader.read("Inputs/10.txt")
    botList = {}
    instructionList = []
    chipList = []
    regexp = re.compile('([a-z]* \d*) gives low to ([a-z]* \d*) and high to ([a-z]* \d*)')

    for line in data:
        if "b" in line[0]:
            match = regexp.match(line)
            botList[match.group(1)] = Bot(match.group(1), match.group(2), match.group(3), botList)
            if "output" in match.group(2):
                botList[match.group(2)] = Output(match.group(2))
            if "output" in match.group(3):
                botList[match.group(3)] = Output(match.group(3))
        else:
            instructionList.append(line)

    regexp = re.compile('value (\d*) goes to ([a-z]* \d*)')
    for instruction in instructionList:
        match = regexp.match(instruction)
        chip = Chip(int(match.group(1)), match.group(2))
        botList[match.group(2)].chips.append(chip)
        chipList.append(chip)

    chipsToMove = True
    while chipsToMove:
        chipsToMove = False
        for bot in botList:
            if "bot" in botList[bot].name and len(botList[bot].chips) == 2:
                if botList[bot].chips[0].value == 61 or botList[bot].chips[1].value == 61:
                    if botList[bot].chips[0].value == 17 or botList[bot].chips[1].value == 17:
                        print botList[bot].name
                botList[bot].giveChips()
                chipsToMove = True

    tot = 1
    for chip in chipList:
        if chip.currentBot == "output 0" or chip.currentBot == "output 1" or chip.currentBot == "output 2":
            tot *= chip.value
    print tot


if __name__ == "__main__":
    run()
