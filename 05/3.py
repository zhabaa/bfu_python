def wr(kid):
    filename = '-'.join(kid)
    kid = ' '.join(kid)
    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
        file.write(kid)


with open('input.txt', 'r', encoding='utf-8') as file:
    people = list(map(lambda x: x.split(), file.read().split('\n')))
    people.sort(key=lambda x: int(x[2]))

young = people[0]
old =  people[-1]

wr(young)
wr(old)