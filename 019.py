try:
    num = int(input("Enter: "))
    print(10 / num)
except ZeroDivisionError:
    print("num can not 0")
except ValueError:
    print("input must exist")
