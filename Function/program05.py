def summ (*number):
    k = 0
    for i in number:
        k += i
    return k
    
print(summ(3, 5, 6, 7))