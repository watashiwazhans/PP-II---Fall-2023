import psycopg2

data = {
    'host' : 'localhost',
    'database' : 'postgres',
    'user' : 'postgres',
    'password' : "grief/0xTi",
    'port' : 22031

}

sql = '''
        CREATE TABLE phonebook(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            number VARCHAR(12)
    );
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

cursor.execute(sql)

cursor.close()
db.commit()
db.close()