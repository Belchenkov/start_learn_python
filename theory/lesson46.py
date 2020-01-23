import sqlite3

db = sqlite3.connect('test_db.sqlite')

cursor = db.cursor()

# cursor.execute("INSERT INTO user (name, email) VALUES ('Иванов Иван', 'ivanov@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Петров Иван', 'petrov@gmail.com')")
cursor.executescript('''
    INSERT INTO users (name, email) VALUES ('John Doe', 'doe@gmail.com');
    INSERT INTO users (name, email) VALUES ('Nick Sand', 'sand@gmail.com');
''')

users = [
    ('User 1', 'user1@gmail.com'),
    ('User 2', 'user2@gmail.com'),
    ('User 3', 'user3@gmail.com')
]

cursor.executemany("INSERT INTO users (name, email) VALUES(?, ?)", users)

db.commit()

db.close()