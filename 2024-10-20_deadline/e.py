import re
from sys import stdin
from collections import Counter

n = int(input().strip())
lines = [s.strip().lower() for s in stdin]

words = Counter()

for line in lines:
    found_words = re.findall(r'[a-zA-Z]+', line)
    for word in found_words:
        words[word] += 1

output_words = sorted(words.items(), key=lambda x: (-x[1], x[0]))[:n]
print(' '.join(i[0] for i in output_words))
