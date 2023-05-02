import psycopg2
from psycopg2 import Error

del_name = input()
try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(
        host='localhost', 
        database='postgres',
        user='postgres',
        password='sadaa197688630'
    )

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