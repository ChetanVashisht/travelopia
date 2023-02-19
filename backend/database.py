import sqlite3

DB_NAME = "travellers.db"

def getDb():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection

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

def insertTraveller(traveller):
    db = getDb()
    cursor = db.cursor()
    statement = """INSERT INTO travellers
                 (name, email, destination, travellercount, budget)
                 VALUES (?, ?, ?, ?, ?)
                 returning id"""
    cursor.execute(statement, [traveller["name"], traveller["email"], traveller["destination"], traveller["travellerCount"], traveller["budget"]])
    row = cursor.fetchone()
    db.commit()
    (insertedId, ) = row if row else None
    traveller['id'] = insertedId
    return traveller

def mapRow(row):
    if row == None:
        return {}
    return dict(zip(row.keys(), row))

def getTraveller(tId):
    db = getDb()
    cursor = db.cursor()
    statement = "SELECT * FROM travellers where id=?"
    cursor.execute(statement, [tId])
    return mapRow(cursor.fetchone())

def getTravellers():
    db = getDb()
    cursor = db.cursor()
    statement = "SELECT * FROM travellers"
    cursor.execute(statement )
    return list(map(mapRow, cursor.fetchall()))

def deleteTraveller(tId):
    db = getDb()
    cursor = db.cursor()
    statement = "DELETE FROM travellers where id=?"
    cursor.execute(statement, [tId])
    db.commit()
    return cursor.fetchone()
