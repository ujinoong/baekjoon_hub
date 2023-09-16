# 6603 로또
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    line = list(map(int, input().strip().split()))
    k = int(line[0])
    if k == 0:
        break

    for case in combinations(line[1:], 6):
        print(' '.join(map(str, case)))
    print('')