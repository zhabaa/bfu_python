def pyramid(n):
    s = [str(x) for x in range(1, n + 1)]

    while n > 0:
        print(' '.join(s[:n]))
        n -= 1


n = int(input('Введите число: '))
pyramid(n)
