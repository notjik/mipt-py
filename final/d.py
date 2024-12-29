n = int(input())
emp = sorted(enumerate(map(int, input().split())), key=lambda x: x[1], reverse=True)
taxis = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])
res = [0] * n
for (e_i, _), (t_i, __) in zip(emp, taxis):
    res[e_i] = t_i + 1
print(' '.join(map(str, res)))
