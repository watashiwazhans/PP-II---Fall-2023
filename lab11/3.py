# Создайте процедуру для вставки множества новых пользователей по списку имен и телефонов. Используйте цикл и оператор 
# if в хранимой процедуре. Проверьте правильность телефона в процедуре и верните все неверные данные.
import psycopg2
from psycopg2 import Error
import re
name = input()
num = input()
contacts = [
    (1, 'Meiram', '87759654547'),
    (6, 'Delnaz', '87774754547'),
    (7, 'Ogurchik', '87788885651'),
    (8, name, num), # incorrect_values
]
incorrect_values = []
pattern = r'^8777[0-9]{7}$|^8747[0-9]{7}$|^8778[0-9]{7}$|^8700[0-9]{7}$|^8707[0-9]{7}$|^8708[0-9]{7}$|^8705[0-9]{7}$|^8775[0-9]{7}$' 
for i in contacts:
    if re.search(pattern, i[2]) == None:
        contacts.remove(i)
        incorrect_values.append(i)
try:
    data = {
    'host' : 'localhost',
    'database' : 'postgres',
    'user' : 'postgres',
    'password' : "grief/0xTi",
    'port' : 22031
    }
    connection = psycopg2.connect(**data)

    cursor = connection.cursor()
    cursor.executemany('CALL add_user(%s, %s, %s)', contacts)
    connection.commit()

except (Exception, Error) as error:
    print("ERROR", error)
finally:
    if connection:
        cursor.close()
        connection.close()
print(f'List of incorrect values is: {incorrect_values}')