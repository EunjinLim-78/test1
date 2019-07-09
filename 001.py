ir = open('title.txt', 'r')
lines = fr.xreadlines()
for line in lines:
    print 'The first line is: ' + line.rstrip()
fr.close()
