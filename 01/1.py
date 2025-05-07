def find_max_min(a, b, c):
    _max = a
    _min = a

    if b > _max:
        _max = b
    if b < _min:
        _min = b

    if c > _max:
        _max = c
    if c < _min:
        _min = c

    return _max, _min


num1, num2, num3 = map(int, input("Введите три числа: ").split())
max_num, min_num = find_max_min(num1, num2, num3)

print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
