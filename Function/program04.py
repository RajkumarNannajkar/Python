def cal (a, b, c):
    if a >= b and a >= c:
        print(f'Highest number : {a}')
    elif b >= a and b >= c:
        print(f'Highest number : {b}')
    else:
        print(f'Highest number : {c}')

j = cal (67,34,23)

k = cal(45, 87, 76)

l = cal (34, 45, 90)