import random


def binomial(m: int, p: float, n: int):
    for i in range(n):
        sum = 0
        for j in range(m):
            r = random.uniform(0, 1)
            sum += int(r <= p)
        yield sum


def geometric(p: float, n: int):
    for i in range(n):
        result = 0
        while random.uniform(0, 1) > p:
            result += 1
        yield result
