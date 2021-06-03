import sys
from typing import List, TextIO, Tuple


def neighbors(g: List[List[int]], r: int, c: int, t: int) -> List[Tuple[int, int]]:
    return [
        (s, d)
        for s, d in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        if 0 <= s < len(g) and 0 <= d < len(g[0]) and g[s][d] == t
    ]


def find_region(grid: List[List[int]], r1: int, c1: int, region_no: int) -> None:
    t = grid[r1][c1]
    frontier = [(r1, c1)]
    grid[r1][c1] = region_no

    while frontier:
        r, c = frontier.pop()
        for s, d in neighbors(grid, r, c, t):
            grid[s][d] = region_no
            frontier.append((s, d))


def find_regions(grid: List[List[int]]) -> None:
    region_no = 2
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] <= 1:
                find_region(grid, r, c, region_no)
                region_no += 1


def solve(grid: List[List[int]], queries: List[Tuple[int, ...]]) -> None:
    ts = [grid[r][c] for r, c, _, _ in queries]
    find_regions(grid)
    for t, (r1, c1, r2, c2) in zip(ts, queries):
        if grid[r1][c1] == grid[r2][c2]:
            print('binary' if t == 0 else 'decimal')
        else:
            print('neither')


def parse(f: TextIO) -> Tuple[List[List[int]], List[Tuple[int, ...]]]:
    rows, cols = [int(x) for x in f.readline().strip().split()]
    grid = [[int(x) for x in f.readline().strip()] for _ in range(rows)]
    m = int(f.readline().strip())
    queries = [tuple(int(x) - 1 for x in f.readline().strip().split()) for _ in range(m)]
    return grid, queries


solve(*parse(sys.stdin))
