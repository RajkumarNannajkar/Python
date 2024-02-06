class Father: #multiple inheritance
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'I am {self.name}')


class Mother:
    def __init__(self, age):
        self.age = age

    def infor(self):
        print(f'I am {self.age} year old')

class Child(Father, Mother):
    def __init__(self, name, age, city):
        Father.__init__(self, name)
        Mother.__init__(self,age)
        self.city = city
    
    def final(self):
        self.info()
        self.infor()
        print(f'I am from {self.city}')


x = Child('Raj', 23, 'Pune')
x.final()