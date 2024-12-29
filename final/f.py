import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
idx = 2
res = 0
dp = [0] * (m + 1)
prev = 0
for i in range(n):
    for j in range(1, m + 1):
        temp = dp[j]
        if data[idx] == '1':
            dp[j] = min(dp[j], dp[j - 1], prev) + 1
            res = max(res, dp[j])
        else:
            dp[j] = 0
        prev = temp
        idx += 1
print(res)