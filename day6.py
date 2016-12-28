import InputReader
"""
Decrypt word by counting how many times each character appears in each position in a word for a list of words
Uses a dictionary for each character position with the character as key and count as value.
"""

class wordDecrypter:
    def __init__(self,wordLength):

        self.dictionaries = [{} for _ in range(wordLength)]

    def addWord(self, word):

        for index in range(0, len(word)-1):  # -1 to skip newline char
            char = word[index]
            if char in self.dictionaries[index].keys():
                self.dictionaries[index][char] += 1
            else:
                self.dictionaries[index][char] = 1

    def getWords(self):
        finalWord = ["",""]
        for dictionary in self.dictionaries:
            # sort by value then key
            orderedList = (sorted(dictionary.items(), key=lambda x: (-x[1], x[0])))
            finalWord[0] += orderedList[0][0]  # most common letter
            finalWord[1] += orderedList[-1][0]  # least common letter
        return finalWord


def run():
    data = InputReader.read("Inputs/6.txt")
    decrypter = wordDecrypter(len(data[0])-1)  # -1 for newline char
    for line in data:
        decrypter.addWord(line)

    correctWords = decrypter.getWords()
    print("The word from most common letters is: {0} \nand for the least common it is: {1}".format(correctWords[0], correctWords[1]))


if __name__ == "__main__":
    run()
