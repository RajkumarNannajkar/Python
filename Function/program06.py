def mul (*numbers):
    k = 1
    for i in numbers:
        k *= i 
    return k 

print(mul(3, 5, 7, 7))

print(mul(3, 5))

s = mul(3,5,6)
print(s)