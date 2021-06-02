import sys


def solve(n, a):
    a.remove(0)
    n -= 1
    happiness = sum((j + 2)*a[j] for j in range(n))
    best = happiness
    for i in range(n):
        happiness += (i + 1)*a[i]
        happiness -= (i + 2)*a[i]
        if happiness > best:
            best = happiness
    print(best)


def parse(f):
    n = int(f.readline().strip())
    a = [int(x) for x in f.readline().strip().split()]
    return n, a


solve(*parse(sys.stdin))
