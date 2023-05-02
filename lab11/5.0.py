# Реализовать процедуру удаления данных из таблиц по имени пользователя или телефону
import psycopg2
from psycopg2 import Error

def create_func(query):
    try:
        connection = psycopg2.connect(
            host='localhost', 
            database='postgres',
            user='postgres',
            password='sadaa197688630'
            )
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Procedure is created')

postgresql_proc = """
CREATE OR REPLACE PROCEDURE delete_user(n_name varchar) 
AS $$ 
BEGIN
    DELETE FROM phonebook WHERE name = n_name;
END;
$$ 
LANGUAGE plpgsql
"""
create_func(postgresql_proc)