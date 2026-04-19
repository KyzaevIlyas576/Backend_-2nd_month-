from lessons.money import Money
from lessons.database import (
    create_tables,
    add_student,
    delete_student,
)
import sqlite3


money_1 = Money(10, 'USD')
# print(money_1)
connection = sqlite3.connect('database.db')
create_tables(connection)
add_student(
    connection,
    "Igor", 35, "Bishkek",
)
# delete_student(connection)
