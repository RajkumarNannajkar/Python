def log (a, b, c):  # middel number return
    if a >= b  and a <= c:
        print(a)
    elif a <=b and a >= c:
        print(a)
    elif  b >= a and b <= c:
        print(b)
    elif b <= a and b >= c:
        print(b)
    elif c >= a and c <= b:
        print(c)
    elif c <= a and c >= b:
        print(c)
    else:
        print('error')


l = log(23, 56, 78)
l 

i = log(77, 56, 78)
i

o = log(34, 55, 33)
o
