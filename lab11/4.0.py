# Создать функцию для запроса данных из таблиц с разбиением на страницы (по пределу и смещению)
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
        print("Error with PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Function is created')


postgresql_func = """
CREATE OR REPLACE FUNCTION pagi2(lim integer, off integer)
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