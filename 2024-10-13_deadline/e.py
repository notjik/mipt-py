from collections import Counter

alpha = Counter(input())
print([value // 2 for key, value in alpha.items() if value > 1])