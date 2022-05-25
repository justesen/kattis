import sys
from typing import TextIO, Tuple, List


def find(x: int, xs: List[int]) -> bool:
    low = 0
    high = len(xs) - 1
    while low <= high:
        mid = (low + high)//2
        if xs[mid] < x:
            low = mid + 1
        elif xs[mid] > x:
            high = mid - 1
        else:
            return True
    return False


def solve(n: int, t: int, xs: List[int]) -> str:
    if t == 1:
        xs.sort()
        for i in range(n):
            if find(7777 - xs[i], xs):
                return 'Yes'
        return 'No'
    if t == 2:
        xs.sort()
        for i in range(n - 1):
            if xs[i] == xs[i + 1]:
                return 'Contains duplicate'
        return 'Unique'
    if t == 3:
        xs.sort()
        median = n // 2
        if xs[0] == xs[median]:
            return str(xs[median])
        median = median if n % 2 == 1 else median - 1
        if xs[median] == xs[n - 1]:
            return str(xs[median])
        return '-1'
    if t == 4:
        xs.sort()
        if n % 2 == 0:
            return f"{xs[n//2 - 1]} {xs[n//2]}"
        return f"{xs[n//2]}"
    if t == 5:
        return ' '.join([str(y) for y in sorted([x for x in xs if 100 <= x <= 999])])
    return ''


def parse(f: TextIO) -> Tuple[int, int, List[int]]:
    n, t = [int(x) for x in f.readline().strip().split()]
    xs = [int(x) for x in f.readline().strip().split()]
    return n, t, xs


print(solve(*parse(sys.stdin)))
