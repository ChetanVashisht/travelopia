import sqlite3

DB_NAME = "travellers.db"

def getDb():
    return sqlite3.connect(DB_NAME)

def createTables():
    tables = [
        """CREATE TABLE IF NOT EXISTS travellers
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        destination TEXT NOT NULL,
        travellercount NUMERIC NOT NULL,
        budget NUMERIC NOT NULL)""",
    ]
    cursor = getDb().cursor()
    for table in tables:
        cursor.execute(table)

createTables()
