import sqlite3
from asyncio.windows_events import NULL


def create_table(conn):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    ''')


def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    print(name)
    conn.execute('''
    INSERT INTO books(name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES
    (?, ?, ?, ?, ?, ?)
    ''',
     (name, author, publication_year, genre, number_of_pages, number_of_copies)
     )
    conn.commit()


if __name__ == '__main__':
    connection = sqlite3.connect('books.db')
    create_table(connection)

    books = [
        ('1984', "Джордж Оруэлл", 1949, "антиутопия", 328, 67),
        ("Стальная крыса", "Гаррри Гаррисон", 1961, "научная фантастика", 256, 134),
        ("Евгений Онегин", "Александр С. Пушкин", 1825, "жанр в стихах", 350, 105),
        ("Приключения Тома Сойера", "Марк Твен", 1876, "приключения", 275, 300),
        ("Вечера на хуторе близ Диканьки", "Николай В. Гоголь", 1832, "повесть", 352, 204),
        ("Зов Ктулху", "Говард Ф. Лавкрафт", 1928, "ужас", 40, 13),
        ("Персеполис", "Маржан Сатрапи", 2013, "автобиография", 352, 152),
        ("Вождь краснокожих", "О. Генри", 1907, "повесть", 65, 4),
        ("Зелёная миля", "Стивен Кинг", 1996, "криминал", 384, 92),
        ("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "фэнтези", 223, 334)
    ]

    for book in books:
        insert_books(connection, *book)
