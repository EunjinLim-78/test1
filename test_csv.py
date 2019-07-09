## print if species == Herpes

with open('test.csv', 'r') as fr:
    fr.readline().strip().split(',')
    for line in fr:
        l = line.strip().split(',')
        id_ = l[0]
        seq_ = l[1]
        species = l[2]
        if species == 'Herpes'
        print(line.strip())

