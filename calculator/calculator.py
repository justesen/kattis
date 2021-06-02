import sys


for line in sys.stdin:
    print(f"{float(eval(line)):.2f}")
