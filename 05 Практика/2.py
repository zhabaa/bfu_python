with open('input.txt', 'r', encoding='utf-8') as file:
    nums = list(map(int, file.readlines()))
    nums.sort()
    
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("\n".join(map(str, nums)))