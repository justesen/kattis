import sys


print(len({int(x) % 42 for x in sys.stdin}))
