def tan (*args):
    k = 1
    for i in args:
        k = i*i
        print(f'{i} of square : {k}')
    return tan

s = tan(4, 9, 8)
n = tan (*range(1, 20))