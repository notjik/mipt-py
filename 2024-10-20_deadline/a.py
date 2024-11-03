from collections import Counter

counter = Counter(input())
res = 0
center = False
for key in counter.keys():
    add = (counter[key] // 2) * 2
    res += add
    counter[key] -= add
    if counter[key] != 0:
        center = True
print(res + (1 if center else 0))