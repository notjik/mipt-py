k = int(input())
bits = list(map(int, input().split()))[:-1]

c = 1
c_bit = bits[0]
res = []
if c_bit == 1:
    res.append(0)
for bit in bits[1:]:
    if bit == c_bit:
        c += 1
        if c > k:
            res.append(k)
            res.append(0)
            c -= k
    else:
        res.append(c)
        c_bit = bit
        c = 1
if c > 0:
    res.append(c)

print(*res)