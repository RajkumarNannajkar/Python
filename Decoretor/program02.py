def cal (func):
    def mul ():
        print('Good morning, Hello How are you')
        func()
        print('Thank you for visit')
    return mul

@cal
def show():
    print("I am Rajkumar,I am fine ")

show()