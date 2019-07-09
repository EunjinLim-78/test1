seq = ''
with open('059.fasta', 'r') as fr:
    if line.startswith('>'):
        pass
    else:
        seq += line.strip()
    print(len(seq))
