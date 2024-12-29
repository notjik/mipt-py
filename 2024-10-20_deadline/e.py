from sys import stdin

trees = {tuple(map(int, s.split())) for s in stdin}

res = float('inf')
for x1, y1 in trees:
    for x3, y3 in trees:
        if (x3, y1) in trees and (x1, y3) in trees:
            s = abs(x3 - x1) * abs(y3 - y1)
            res = min(res, s) if s != 0 else res

print(res if res != float('inf') else 0)
