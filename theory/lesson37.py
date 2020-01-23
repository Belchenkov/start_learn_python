# from classes import Person ???


class Person:
    name = 'John'

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f'Hello, my name is {self.name}')



person1 = Person('Mark')
person1.print_info()
person2 = Person('John')
person2.print_info()