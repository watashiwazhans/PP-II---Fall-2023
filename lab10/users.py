import psycopg2

data = {
    'host' : 'localhost',
    'database' : 'postgres',
    'user' : 'postgres',
    'password' : "grief/0xTi",
    'port' : 22031
}
conn = psycopg2.connect(**data)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER NOT NULL,
    score INTEGER NOT NULL);
""")

cur.execute("""
 INSERT INTO users (username, level, score) 
 VALUES ('Zhans', 0, 0), ('Altynbek', 0, 0);
""")

conn.commit()

cur.close()
conn.close()