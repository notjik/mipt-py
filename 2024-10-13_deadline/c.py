n = int(input())
is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
print("True" if is_leap(n) else f"False {min(filter(is_leap, range(n - 4, n + 4)), key=lambda x: (abs(n - x), x))}")
