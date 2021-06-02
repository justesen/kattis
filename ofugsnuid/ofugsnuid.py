import sys


n = int(sys.stdin.readline())
for x in reversed([x.strip() for x in sys.stdin]):
    print(x)
