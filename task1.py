a = [int(i) for i in input("Введите целые числа: ").split()]
b = int(input("Введите число: "))


def large(a=[]):
    a.sort()
    c = []
    for i in range(len(a)):
        if a[i] >> b:
            c.append(a[i])
    return c


print(large(a))
