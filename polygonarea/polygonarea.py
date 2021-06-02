import sys


def solve(n, points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    area = sum(x[i]*y[(i+1) % n] - x[(i+1) % n]*y[i] for i in range(len(points)))/2

    if area > 0:
        print(f"CCW {area:.1f}")
    else:
        print(f"CW {-area:.1f}")


def parse(f):
    while True:
        n = int(f.readline().strip())
        if n == 0:
            break
        points = [
            tuple(int(c) for c in f.readline().strip().split())
            for _ in range(n)
        ]
        yield n, points


for n, points in parse(sys.stdin):
    solve(n, points)
