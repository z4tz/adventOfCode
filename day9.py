import gc
import objgraph
import sys
import resource

import InputReader


class decompressor:
    def __init__(self):
        self.compressedText = ""
        self.decompressedText = ""
        self.currentPosition = 0
        self.textList = []

    def start(self, text):
        self.currentPosition = 0
        self.compressedText = text
        textLength = len(self.compressedText)
        completion=0

        while self.currentPosition < textLength:
            if self.compressedText[self.currentPosition] == '(':
                self.expandTextHere()
            else:
                self.textList.append(self.compressedText[self.currentPosition])
                self.currentPosition += 1

            percent = int(self.currentPosition*1.0/textLength*100)
            if percent != completion:
                completion=percent
                print("{0}%".format(completion))

        if len(self.compressedText) < 2000000000:
            self.decompressedText = ''.join(self.textList)
            self.textList = []
        else:
            tot = 0
            print"------"
            for line in self.textList:
                if '(' in line:
                    print "not done"
                tot += len(line)
            print tot
            return ""

        return self.decompressedText

    def expandTextHere(self):
        endPosition = self.currentPosition
        while not self.compressedText[endPosition] == ')':
            endPosition += 1
        split = self.compressedText[self.currentPosition + 1:endPosition].split('x')
        extendLength = int(split[0])
        repeat = int(split[1])
        self.textList.append(self.compressedText[endPosition + 1:endPosition + extendLength + 1] * repeat)

        self.currentPosition = endPosition + extendLength + 1


def run():
    data = InputReader.read("Inputs/9.txt")
    data = data[0]
    decomp = decompressor()
    while '(' in data:
        print("{0} MB".format( sys.getsizeof(data)/1000000))
        data = decomp.start(data)
        print len(data)


if __name__ == "__main__":
    run()
