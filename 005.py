num1 = 21
if num1 % 3 == 0 and num1 % 7 == 0:
    print(num1, '3 and 7 multiple')
elif num1 % 3 == 0:
    print(num1, '3 multiple')
elif num1 % 7 == 0:
    print(num1, '7 multiple')
else:
    print(num1, 'not 3 and 7 multiple')
