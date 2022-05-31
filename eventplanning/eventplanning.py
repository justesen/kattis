import sys
from typing import List, TextIO, Tuple


def solve(n: int, b: int, w: int, hotels: List[Tuple[int, List[int]]]) -> None:
    best_price = b + 1
    for p, weeks in hotels:
        if n*p < best_price and next((w for w in weeks if w >= n), False):
            best_price = n*p
    if best_price <= b:
        print(best_price)
    else:
        print("stay home")


def parse(f: TextIO) -> Tuple[int, int, int, List[Tuple[int, List[int]]]]:
    n, b, h, w = [int(x) for x in f.readline().strip().split()]
    hotels = []
    for _ in range(h):
        p = int(f.readline())
        weeks = [int(x) for x in f.readline().strip().split()]
        hotels.append((p, weeks))
    return n, b, w, hotels


solve(*parse(sys.stdin))
