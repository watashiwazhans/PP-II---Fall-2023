import psycopg2
data = {
    'host' : 'localhost',
    'database' : 'postgres',
    'user' : 'postgres',
    'password' : "grief/0xTi",
    'port' : 22031

}
config = psycopg2.connect(**data)
config.autocommit = True
cursor = config.cursor()
  
sql = '''SELECT * from phonebook where name LIKE '%i%' '''
  
cursor.execute(sql)

for i in cursor.fetchall():
    print(*i)
  
config.commit()
config.close()