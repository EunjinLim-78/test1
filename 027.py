Seq1 = 'ATGTTATAG'
revSeq1 =''
for i in range (len(Seq1)-1,-1,-1):
    revSeq1 += Seq1[i]
print(revSeq1)


Seq1 = 'ATGTTATAG'
revSeq1 = Seq1[::-1]
print(revSeq1)

