"""Create a DAO (data access object)."""
# this thing should do

# google python dataclass
import sqlite3


class JellyfishDao:
    def __init__(self, filename: str):
        """Creates a DAO for jellyfish."""
        self.filename = filename
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Jellies(name VARCHAR PRIMARY KEY, color VARCHAR, size INTEGER)"
        )
        self.connection.commit()
        self.connection.close()

    def add(self, name: str, color: str, size: int):
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Jellies VALUES (?,?,?)", (name, color, size))
        self.connection.commit()
        self.connection.close()

    def get(self, jellyname: str):
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        jelly = self.cursor.execute(
            "SELECT name, color FROM Jellies WHERE name = ?", (jellyname,)
        ).fetchall()
        self.connection.close()
        return jelly

    def list(self):
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        jellylist = self.cursor.execute(
            "SELECT name, color, size FROM Jellies"
        ).fetchall()
        self.connection.close()
        return jellylist


jellydao = JellyfishDao("Jellies.db")

print(jellydao.get("alfero"))
print(jellydao.list())
