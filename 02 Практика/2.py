s = input('>> ')
d = dict()

for i in s:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

print(sorted(d.items(), key=lambda x: x[1], reverse=True)[:3])
