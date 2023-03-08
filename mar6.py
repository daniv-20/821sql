import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE Users")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Users(name VARCHAR PRIMARY KEY, dob INTEGER, pw BLOB)"
)
cursor.executemany(
    "INSERT INTO Users VALUES(?,?,?)",
    [
        ("Patrick", 1970, "helloworld"),
        ("Richard", 1994, 3.14),
        (123, 2012, None),
        ("Pat", 2021, "pw"),
    ],
)

connection.commit()
c = cursor.execute(
    "SELECT name, pw FROM Users WHERE name = ?", ("Patrick",)
)  ##trailing comma is tuple w/ 1 element
data = c.fetchall()
print(data)
connection.close()
