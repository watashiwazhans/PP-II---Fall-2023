import psycopg2
data = {
    'host' : 'localhost',
    'database' : 'postgres',
    'user' : 'postgres',
    'password' : "grief/0xTi",
    'port' : 22031
}
config = psycopg2.connect(**data)

current = config.cursor()
# добавляем значения в таблицу 
id = 3
name = 'Darina'
number = '87071213596'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()