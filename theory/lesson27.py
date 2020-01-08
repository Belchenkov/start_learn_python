# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#

# print(get_sum(1, 2, 5, 7))
# print('hello', sep='', end='')

# print(get_sum(1, 2, d=4))


# def get_sum(*args):
#     return sum(args)
#
#
# print(get_sum(1, 5, 10)


# def func(**kwargs):
#     print(kwargs)
#
#
# func(a=1, b=5, c=20)


def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)


f(1, 2, 3, 4, b='test', c='hi')