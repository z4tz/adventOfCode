import sys
import InputReader

"""
Horrible solution made just to see if it worked, took about 25GB of memory to decompress whole thing but it worked
TODO: Remake with a recursive version that only counts values and doesnt store the actual string.
"""
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
        self.endPosition = self.currentPosition
        while not self.compressedText[self.endPosition] == ')':
            self.endPosition += 1
        self.split = self.compressedText[self.currentPosition + 1:self.endPosition].split('x')
        self.textList.append(self.compressedText[self.endPosition + 1:self.endPosition + int(self.split[0]) + 1] * int(self.split[1]))

        self.currentPosition = self.endPosition + int(self.split[0]) + 1


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
