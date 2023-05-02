import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='sadaa197688630'
)

current = config.cursor()
# добавляем значения в таблицу 
id = 1
name = 'Daniar'
number = '87774659300'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()