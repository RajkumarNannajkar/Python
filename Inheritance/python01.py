class Person:  #inheritance sigal methon
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info (self):
        print(f'I am {self.name} and my age is {self.age}')
    
class Student(Person):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city

    def City(self):
        super().info()
        print(f"I am from {self.city}")

x = Student('Raj', 27, 'Pune')
x.City()

y = Student('kedar', 34, 'narhe')
y.City()