from collections import deque

s = input().strip()
stack = deque()
brackets = {')': '(', '}': '{', ']': '[', '>': '<'}
for i, c in enumerate(s):
    if c in brackets.values():
        stack.append(c)
    elif c in brackets.keys():
        if not stack or brackets[c] != stack.pop():
            print(f"False {i + 1}")
            break
else:
    if stack:
        print(f"False {len(s)}")
    else:
        print("True")
