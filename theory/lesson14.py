# year = 1900
# while year <= 2019:
#     print(year)
#     year += 1
# else:
#     print('Done')
#
# l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
#
# l2 = list('hello')
# l3 = list((1, 2, 3))
# l4 = [i for i in 'hello']
# l5 = [i*2 for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]

# l6 = list(range(0, 11, 2))
# print(l6)

for i in range(1, 3):
    print(f'Внешний цикл #{i}')
    for j in range(1, 3):
        print(f'\tВнутренний цикл #{j}')