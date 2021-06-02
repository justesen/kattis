import sys


def solve(case, n, nums, m, queries):
    print(f"Case {case + 1}:")
    for case, q in enumerate(queries):
        best = None
        for i in range(n):
            for j in range(i + 1, n):
                attempt = nums[i] + nums[j]
                if not best or abs(q - attempt) < abs(q - best):
                    best = attempt
        print(f"Closest sum to {q} is {best}.")


def parse(f):
    line = f.readline().strip()
    while line:
        n = int(line)
        nums = [int(f.readline().strip()) for _ in range(n)]
        m = int(f.readline().strip())
        queries = [int(f.readline().strip()) for _ in range(m)]
        yield n, nums, m, queries
        line = f.readline().strip()


for case, args in enumerate(parse(sys.stdin)):
    solve(case, *args)
