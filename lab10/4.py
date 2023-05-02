import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = 'sadaa197688630',
    user = 'postgres'
)

current = config.cursor()

sql = '''
    INSERT INTO phonebook
    VALUES (%s, %s, %s);
'''
# вставляем данные в телефонную книгу вводя их с консоли

print("ID:")
id = int(input())
print("Name:")
username = input()
print("Phone number:")
number = input()
current.execute(sql, (id, username, number))

current.close()
config.commit()
config.close()