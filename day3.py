import InputReader


class triangleComparer:
    def __init__(self):
        self.valid = 0

    def compare(self,sides):
        longestSide = max(sides)
        if longestSide < sum(sides) - longestSide:
            self.valid += 1


def run():
    data = InputReader.read("Inputs/3.txt")
    comparer = triangleComparer()
    for line in data:
        comparer.compare([int(line[0:5]), int(line[6:10]), int(line[11:15])])
    print("Number of valid triangles: {0}".format(comparer.valid))

    comparer2 = triangleComparer()
    for index in range(0,len(data)/3):
        for col in range(0, 3):
            comparer2.compare([int(data[index*3][1+col*5:5+col*5]), int(data[index*3+1][1+col*5:5+col*5]), int(data[index*3+2][1+col*5:5+col*5])])
    print("Number of valid triangles using c: {0}".format(comparer2.valid))


if __name__ == "__main__":
    run()
