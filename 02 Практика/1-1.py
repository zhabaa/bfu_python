def decompress_string(s):
    result = []
    i = 0

    while i < len(s):
        char = s[i]
        i += 1
        count = ''
        
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        
        if count:
            result.append(char * int(count))

        else:
            result.append(char)

    return ''.join(result)


s = input('>> ')
decompressed_s = decompress_string(s)
print(decompressed_s)
