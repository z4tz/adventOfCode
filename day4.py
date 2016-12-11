import InputReader
import re


class roomChecker:
    def __init__(self):
        self.validSum = 0

    def validateRoom(self,line):
        [chars, roomId, checksum] = self.extractData(line)
        calcChecksum = self.calcChecksum(chars)
        if checksum == calcChecksum:
            self.validSum += int(roomId)
            if 'northpole' in self.shiftString(chars, int(roomId)):
                print("northpole object storage in room with ID: {0}".format(roomId))



    def calcChecksum(self,chars):
        # creates the checksum string made from the 5 most commonly occurring characters
        chars = chars.replace('-', '')
        counts = {}
        for char in chars:
            if char in counts.keys():
                counts[char] +=1
            else:
                counts[char] = 1
        # sorts the dictionary first after number of occurrences (- to get reverse),
        # secondary sort on key in alphabetical order
        orderedList = (sorted(counts.items(), key=lambda x: (-x[1], x[0])))

        checkSum = ''
        for i in range(0,5):
            checkSum += orderedList[i][0]
        return checkSum

    def extractData(self,line):
        match = re.match('([a-z-\-]+)([0-9]+)\[([a-z]+)\]', line)
        return match.groups()

    def shiftString(self, string, shiftAmmount):
        newString = ''
        for char in string:
            if char is '-':
                newString += ' '
            else:
                newString += self.shiftChar(char,shiftAmmount)
        return newString


    def shiftChar(self,char,ammount):
        # 26 chars, a = 97
        newChar = chr(97 + (ord(char)- 97 + ammount) % 26)
        return newChar


def run():
    data = InputReader.read("Inputs/4.txt")
    checker = roomChecker()
    for line in data:
        checker.validateRoom(line)

    print("Sum of valid roomIDs: {0}".format(checker.validSum))

if __name__ == "__main__":
    run()
