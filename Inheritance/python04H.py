class Father:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f'I am {self.name}')

class child1(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def age_info(self):
        self.info()
        print(f'I am {self.age} year old')

class child2(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def age_info1(self):
        self.info()
        print(f'I am {self.age} year old')


x = child1("Raj" , 23)
x.age_info()

y = child2('vishal', 22)
y.age_info1()
