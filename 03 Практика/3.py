arr = list(map(str, input().split()))

d = dict()

for elem in arr:
    if elem not in d.keys():
        d[elem] = 1
    else:
        d[elem] += 1

print(*d.values())
