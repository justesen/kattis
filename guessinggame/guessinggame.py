import sys


f = sys.stdin
high = 11
low = 0

while True:
    guess = int(f.readline().strip())
    if guess == 0:
        break
    response = f.readline().strip()
    if response == 'right on':
        if low < guess < high:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        high = 11
        low = 0
    elif response == 'too high' and guess < high:
        high = guess
    elif response == 'too low' and guess > low:
        low = guess
