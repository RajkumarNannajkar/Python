class Gfather: # multilevel inheritance method
    def __init__(self, name):
        self.name = name
    
    def info (self):
        print(f'I am {self.name}')

class Father(Gfather):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def infor (self):
        print(f'I am {self.age} year old')

class Child (Father):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city
    
    def inform (self):
        self.info()
        self.infor()
        print(f'I am from {self.city}')

x = Child('Raj', 27, 'Pune')
x.inform()

        