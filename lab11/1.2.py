import psycopg2
from psycopg2 import Error

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
    # хранимая процедура
    cursor.callproc('pattern')
    result = cursor.fetchall()
    for row in result:
        print("id = ", row[0])
        print("name = ", row[1])
        print("number = ", row[2])

except (Exception, Error) as error:
    print("ERROR", error)
finally:
    if connection:
        cursor.close()
        connection.close()
#select * from phonebook order by id desc
#select * from phonebook order by 