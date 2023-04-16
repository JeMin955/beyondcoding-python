import sys
import math

input = sys.stdin.readline

def isPrime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
for i in range(N):
    x = int(input())
    while True:
        if isPrime(x):
            print(x)
            break
        else:
            x += 1