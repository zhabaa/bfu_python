def prod(arr: list):
    result = 1

    for i in arr:
        result *= i

    return result


with open("input.txt", "r", encoding="utf-8") as file:
    nums = list(map(int, file.readline().split()))
    _prod = prod(nums)


with open("output.txt", "w", encoding="utf-8") as file:
    file.write(str(_prod))
