def tan (*args):
    k = 0
    for i in args:
        k += i
        print(k)
    return tan

s = tan(4, 9, 8)
n = tan (*range(1, 20))