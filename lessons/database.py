def create_tables(conn):
    # запрос на создание таблицы
    conn.execute('''
    CREATE TABLE IF NOT EXISTS students(
        name TEXT,
        age INTEGER,
        city TEXT
    )
    ''')

def add_student(conn, name, age, city):
    print(name, age, city)
    conn.execute('''
    INSERT INTO students
    VALUES
    (?, ?, ?)
    ''',
    (name, age, city)
    )
    conn.commit()

def delete_student():
    ...
