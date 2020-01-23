class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'quest'

    def say_hi(self):
        return 'Hi'

    def say_hi2(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name


a = A()
# a.property1 = 'Property 1'
# a.property2 = 'Property 2'
#
# print(a.property1)
# print(a.property2)

print(a.say_hi2('John'))