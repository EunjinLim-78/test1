'''
    -- 0, (n=1)
f()n-- 1, (n=2)
    -- f(n-2) + f(n-1), (others)
    '''

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

for i in range(1,11,1):
    print(i,fib(i))

'''
[0, 1]
.append(-1, -2)
-> [0, 1, 1]
'''
'''
l = [0, 1, 1]
for i in range(8)
    val = l[-2] + l[-1]
    l.append(val)
print(l)
