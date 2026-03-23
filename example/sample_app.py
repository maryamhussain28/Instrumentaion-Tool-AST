def compute(x):
    total = 0
    for i in range(x):
        total += i
    return total


def process():
    compute(10000)
    compute(20000)


process()