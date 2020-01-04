# def get_sum(a, b):
#     """
#     Возвращает сумму аргументов а и b.
#
#     :param a: Первый операнд
#     :type a: int
#     :param b: Второй операнд
#     :type b: int
#     :return: Return type int
#     """
#     return a + b
#
#
# print(get_sum(1, 2))
#
a = 5 #global
#
#
# def f():
#     a = 10
#     a += 1
#     print(a)
#
#
# print(a)
# f()


# def f():
#     global a
#     a += 1
#
# print(a)
# f()
# print(a)


l = [1, '2', 3]


# def f(l):
#     return [i * 2 for i in l]
#
#
# print(f(l))


# def f2(l):
#     def get_mult(x):
#         return x * 2
#     return [get_mult(i) for i in l]
#

# def f3(l):
#     def get_mult(x):
#         if isinstance(x, int):
#             return x * 2
#     return [get_mult(i) for i in l if get_mult(i)]
#
#
# print(f3(l))


def f4(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))


print(f4(l))


