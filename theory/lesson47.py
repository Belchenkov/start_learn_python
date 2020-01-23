import sqlite3

db = sqlite3.connect('test_db.sqlite')

cursor = db.cursor()

email = 'doe@gmail.com'

# cursor.execute("SELECT * FROM users WHERE email = ?", [email])
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, 'John Doe'))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': 'John Doe'})
cursor.execute("SELECT * FROM users")

res = cursor.fetchall()

print(res)

for user in res:
    print(res[1], res[2])

db.close()