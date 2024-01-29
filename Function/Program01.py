def mul(*kwargs):
    c = []
    for i in kwargs:
        c.append(i * i)
    return c

result = mul(*range(1, 10))
print(result)
