import sys


def solve(stacks):
    for stack in stacks:
        count = 0
        searching_for = 1
        for dvd in stack:
            if dvd != searching_for:
                count += 1
            else:
                searching_for += 1
        print(count)


def parse(f):
    k = int(f.readline().strip())
    stacks = []
    for _ in range(k):
        _n = int(f.readline().strip())
        stacks.append([int(x) for x in f.readline().strip().split()])
    return stacks


solve(parse(sys.stdin))
