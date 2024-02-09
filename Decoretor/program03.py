def welcome (func):
    def good():
        print('Welcome')
        func()
        print('Thank You')
    return good

def genderSelection():
    print('select Your gender (M/F)')
    gender = input()
    return gender

@welcome
def show():
    flag=True
    name = input("Enter your name :  ")
    age = int(input('Enter your age :  '))
    while flag:
        gender = genderSelection()
        if gender is 'M' or gender is 'F':
            flag=False
    disply_information(name,age,gender)

def disply_information(name,age,gender):
    print('Your name is ',name)
    print('Your age is ',age)
    print('Your gender is ',gender)




show()