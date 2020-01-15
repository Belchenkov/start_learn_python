class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')


class Employee(Person):
    company = 'Google'

# person2 = Person('John')
employee = Employee('John', 25)
print(employee.print_info())
