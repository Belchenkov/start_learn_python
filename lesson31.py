from datetime import date, datetime, timedelta
import locale

# date
# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday())

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# datetime
now = datetime.now()
# now2 = datetime.today()

# print(now)
# # print(now2)
# print(now.day)
# print(now.month)
# print(now.year)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.weekday)

# print(now.strftime('%a'))
# print(now.strftime('%A'))

# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')

# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

print(now + timedelta(days=1, hours=2, minutes=10))