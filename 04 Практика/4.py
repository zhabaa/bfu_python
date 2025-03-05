def foo(string: str) -> dict:
    d = dict()

    for char in string:
        key = int(char)

        if key not in d.keys():
            d[key] = 1
        else:
            d[key] += 1

    result = dict(sorted(d.items(), key=lambda x: x[1], reverse=True)[:3])

    return result

string = input()
print(foo(string))
