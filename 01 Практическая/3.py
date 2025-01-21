def pascal_triangle_row(n):
    row = [1]

    for k in range(1, n + 1):
        next_value = row[k - 1] * (n - k + 1) // k
        row.append(next_value)

    return row


def print_pascal_triangle(n):
    for i in range(n):
        print(*pascal_triangle_row(i))


print_pascal_triangle(10)
