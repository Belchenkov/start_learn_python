product1 = {
    'title': 'Sony',
    'price': 10
}
product2 = dict(title='iPhone', price=110)
#
# users = [
#     ['bob@gmail.com', 'Bob'],
#     ['katy@gmail.com', 'Katy'],
#     ['john@gmail.com', 'John']
# ]

# product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)

# nums = {i: i + 1 for i in range(1, 10)}


# print(product2['price'])
# print(product2.get('title'))
#
# for key in product1:
#     print(product1[key])

# for key, value in product1.items():
#     print(key, value)
#
# products = [
#     {
#         'title': 'Sony',
#         'price': 10
#     },
#     {
#         'title': 'Samsung',
#         'price': 101
#     }
# ]
products = [
   product1,
   product2
]

for product in products:
    print(product['title'], product['price'])

# print(products)