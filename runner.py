import timeit

days = xrange(1, 2)



if __name__ == '__main__':
    for day in days:
        print("Time used for assignment {0}: {1}s".format(day, timeit.timeit("run()", setup="from day{0} import run".format(day), number=1)))