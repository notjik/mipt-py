from sys import stdin

emails = [s.strip().split("@") for s in stdin]
res = set()
for local, domain in emails:
    res.add((local.split("+")[0].replace(".", ""), domain))
print(len(res))