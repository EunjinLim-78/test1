#l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
#l = 'ATGATGDDTAGCC'
l = 'RKAAPLLOVV'
d = {} ## key: number, value: frequency

for i in l:
    print(1, d)
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

for k, v in d.items():
    print(k, v)
