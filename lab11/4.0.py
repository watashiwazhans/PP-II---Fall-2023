# Создать функцию для запроса данных из таблиц с разбиением на страницы (по пределу и смещению)
import psycopg2
from psycopg2 import Error

def create_func(query):
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
        cursor.execute(query)
        connection.commit()

    except (Exception, Error) as error:
        print("Error with PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Function is created')


postgresql_func = """
CREATE OR REPLACE FUNCTION pagination(lim integer, off integer)
    RETURNS TABLE(id integer, name varchar, number varchar) 
    AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook LIMIT lim OFFSET off;
END;
$$ 
LANGUAGE plpgsql;
"""
create_func(postgresql_func)