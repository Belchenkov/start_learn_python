"""
Дан список words.
Составьте из него список слов-палиндромов.
 Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
"""
# words = ['мадам', 'топот', 'test', 'madam', 'word']
# palindromes = []
#
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)

# palindromes = [word for word in words if word == word[::-1]]


# Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
# my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# palindromes = []
#
# for word in my_str:
#     word_r = word.replace(' ', '').lower()
#     if word_r == word_r[::-1]:
#         palindromes.append(word)
#
# print(palindromes)

l = list(range(1, 10))
l2 = list('hello')

# s = '-'.join(l2)
s = '-'.join(map(str, l))

print(s)