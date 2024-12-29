t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print("Artur") if not (n % (k + 1)) else print("Pasha")