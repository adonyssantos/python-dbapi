import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        age INTEGER
    )
""")

cursor.execute("""
    INSERT INTO test (first_name, last_name, age)
    VALUES ('Adonys', 'Santos', 18)
""")

cursor.execute("""
    INSERT INTO test (first_name, last_name, age)
    VALUES ('Samuel', 'Santos', 13)
""")

cursor.execute("""
    SELECT * FROM test
""")

response = cursor.fetchall()

print(response)

conn.close()
