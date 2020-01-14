class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 20  #  private
        # self._age = 20  # protected

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Wrong age')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')

#
# person1 = Person('Mark')
# person1.print_info()

person2 = Person('John')
# print(person2.get_age())
# person2.set_age(24)
# person2._age = 30
# person2.__age = 30
print(person2.age)
person2.age = 33
person2.print_info()