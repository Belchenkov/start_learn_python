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

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def more_info(self):
        print(f'{self.name} work in {self.company}')

    def print_info(self):
        super().print_info()
        print(f'Work: {self.company}')

    def __str__(self):
        # return f'Name: {self.name}'
        return f'Class: {self.__class__.__name__}'


employee = Employee('Nick', 30, 'Google')
employee.print_info()
employee.more_info()
print(employee)