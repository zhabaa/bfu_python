def inverted_pyramid(n):
    for i in range(n, 0, -1):
        d = ' '.join(str(x) for x in range(i, 0, -1))
        a = ' '.join(str(x) for x in range(2, i + 1))
        line = d + (' ' + a if a else '')

        print(line.center((n + 1) * 4))


n = int(input("Введите натуральное число n: "))
inverted_pyramid(n)
