a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(len(set(a).intersection(set(b))))
