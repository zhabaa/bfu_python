arr = list(map(int, input().split()))

max_ = arr.index(max(arr))
min_ = arr.index(min(arr))

arr[max_], arr[min_] = arr[min_], arr[max_]

print(arr)
