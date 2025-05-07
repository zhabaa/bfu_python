arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    if arr[i - 1] < arr[i]:
        print(arr[i])
