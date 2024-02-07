def Tip(a, b, c):
    if a >= b and a >= c and b >= c:
        print((a+b) + (c-b))
    elif c >= a and  c >= b and b >= a:
        print((c+b) + (a-b))
    elif b >= a and  b >= c and a >= c:
        print((b+a) + (c-a))
    elif a >= c and a >= b and c >= b:
        print((a+c) + (b-c))
    elif c >= a and  c >= b and a >= b:
        print((c+a) + (b-a))
    elif b >= a and  b >= c and c >= a:
        print((b+c) + (a-c))
    else:
        print('error')

s = Tip (8, 4, 6)
s

t = Tip (-3, -5, 8)
t

k = Tip (99, 100, 65)
k