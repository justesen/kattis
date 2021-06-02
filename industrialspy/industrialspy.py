import math
import sys

from typing import List, Optional


def powerset(seq):
    """Generate all subsets of seq"""
    if len(seq) <= 0:
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item


def next_permutation(a: List[str]) -> Optional[List[str]]:
    """Return next permutation of a

    Algorithm:
    - Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    - Find the largest index l greater than k such that a[k] < a[l].
    - Swap the value of a[k] with that of a[l].
    - Reverse the sequence from a[k + 1] up to and including the final element a[n].
    """
    for i in range(len(a) - 2, -1, -1):
        if a[i] < a[i+1]:
            for j in range(len(a) - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    a = a[:i+1] + a[-1:i:-1]
                    return a
    return None


def is_prime(x: int) -> bool:
    """Return True iff x is prime"""
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0:
        return False
    for p in range(3, int(math.sqrt(x)) + 1, 2):
        if x % p == 0:
            return False
    return True


def solve(digits: List[str]):
    nums = set()
    for s in powerset(digits):
        while s:
            nums.add(int(''.join(s)))
            s = next_permutation(s)
    print(sum(1 for x in nums if is_prime(x)))


def parse(f) -> List[List[str]]:
    n = int(f.readline().strip())
    cases = []
    for _ in range(n):
        cases.append([c for c in f.readline().strip()])
    return cases


for digits in parse(sys.stdin):
    solve(sorted(digits))
