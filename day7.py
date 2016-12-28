import InputReader
import regex as re  # new regex package that supports overlapping matches.

class ipSnooper:
    def __init__(self):
        self.tlsCount = 0
        self.sslCount = 0
        self.tlsRegex = re.compile(r'(.)(.)\2\1')
        self.sslRegex = re.compile(r'(.)(.)\1')

    def checkIP(self, line):
        split = line.split('[')
        ips =[]
        hyperSequences = []

        ips.append(split[0])
        for index in range(1, len(split)):  #skip first as it does not contain a ']'
            hyperSplit = split[index].split(']')
            hyperSequences.append(hyperSplit[0])
            ips.append(hyperSplit[1])

        self.checkForTLS(hyperSequences, ips)
        self.checkForSSL(hyperSequences, ips, line)

    def checkForTLS(self, hyperSequences, ips):
        # if we find a match in the hyperSequence we can skip forward
        for sequence in hyperSequences:
            seqMatch = self.tlsRegex.findall(sequence, overlapped=True)
            if len(seqMatch) > 0 and seqMatch[0][0] != seqMatch[0][1]:  # sort out aaaa types as well
                return

        for ip in ips:
            match = self.tlsRegex.findall(ip, overlapped=True)
            if len(match) > 0 and match[0][0] != match[0][1]:  # sort out aaaa types as well
                self.tlsCount += 1
                return

    def checkForSSL(self, hyperSequences, ips, line):
        for ip in ips:
            matches = self.sslRegex.findall(ip, overlapped=True)
            for match in matches:
                if match[0] != match[1]:
                    for sequence in hyperSequences:
                        # create a new regex with the exact letters to find.
                        seqMatch = re.findall(r'({0})({1})\1'.format(match[1], match[0]), sequence)
                        if len(seqMatch) > 0:
                            self.sslCount += 1
                            return


def run():
    data = InputReader.read("Inputs/7.txt")
    snooper = ipSnooper()
    for line in data:
        snooper.checkIP(line)

    print("The number of IPs that support TLS is: {0} \nand the number of IPs that support SSL is: {1}".format(snooper.tlsCount, snooper.sslCount))

if __name__ == "__main__":
    run()