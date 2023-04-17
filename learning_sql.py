import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS Users")
cursor.execute("DROP TABLE IF EXISTS Orgs")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Users(name VARCHAR PRIMARY KEY, dob INTEGER, pw BLOB, org_name VARCHAR, FOREIGN KEY(org_name) REFERENCES Orgs(name))"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Orgs(name VARCHAR PRIMARY KEY, location VARCHAR)"  ## user doesn't have location but there is an implied location for each user
)
connection.commit()
cursor.executemany(
    "INSERT INTO Users VALUES(?,?,?, ?)",
    [
        ("Patrick", 1970, "helloworld", "Duke"),
        ("Richard", 1994, 3.14, "UNC"),
        (123, 2012, None, "UNC"),
        ("Pat", 2021, "pw", "Duke"),
        ("Max", 2200, "werp", "asdf"),
    ],
)
cursor.executemany(
    "INSERT INTO Orgs VALUES(?,?)",
    [("Duke", "Durham"), ("UNC", "Chapel Hill"), ("NC State", "Raleigh")],
)

connection.commit()
c = cursor.execute(
    "SELECT name, pw, org_name FROM Users WHERE name = ?", ("Max",)
)  ##trailing comma is tuple w/ 1 element
data = c.fetchall()
print(data)

with connection as cursor:
    cursor.execute("DELETE FROM Users WHERE name=?", ("Max",))
    c = cursor.execute(
        "SELECT Users.name, location FROM Users JOIN Orgs ON Users.org_name=Orgs.name",  ## by default, inner join (intersection/ "and")
    )  ##trailing comma is tuple w/ 1 element
data = c.fetchall()
print(data)

connection.close()
