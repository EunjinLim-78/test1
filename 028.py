Seq1 = 'ATGTTATAG'
newSeq1 = ''
for s in Seq1:
    if s == 'A':
        newSeq1 += 'T'
    elif s == 'T':
        newSeq1 += 'A'
    elif s == 'G':
        newFeq1 += 'C'
    elif s == 'G':
        newSeq1 += 'C'

print(Seq1)
print(newSeq1)

'''
Seq1 = 'ATGTTATAG'
compSeq = ''
comDic = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}

for s in Seq1:
    compSeq += compDic[s]

print(compSeq)
print(newSeq)
