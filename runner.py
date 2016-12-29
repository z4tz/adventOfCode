import timeit
import os

days = xrange(9, 10)


if __name__ == '__main__':
    for day in days:
        print("-----## Assignment day {0} ##-----".format(day))
        print("Time used for assignment {0}: {1}s\n\n".format(day, timeit.timeit("run()", setup="from day{0} import run".format(day), number=1)))