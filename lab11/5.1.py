import psycopg2
from psycopg2 import Error

del_name = input()
try:
    # Подключиться к существующей базе данных
    data = {
    'host' : 'localhost',
    'database' : 'postgres',
    'user' : 'postgres',
    'password' : "grief/0xTi",
    'port' : 22031
    }
    connection = psycopg2.connect(**data)
    cursor = connection.cursor()
    cursor.execute('CALL delete_user(%s)', (del_name,))
    connection.commit()

except (Exception, Error) as error:
    print("ERROR", error)
finally:
    if connection:
        print("User is deleted!")
        cursor.close()
        connection.close()