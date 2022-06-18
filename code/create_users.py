import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

CREATE_QUERY = "CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY,username TEXT,password TEXT)"
cursor.execute(CREATE_QUERY)

CREATE_ITEM = "CREATE TABLE IF NOT EXISTS items (ID INTEGER PRIMARY KEY,name TEXT,price REAL)"
cursor.execute(CREATE_ITEM)

INSERT_ITEM ="INSERT INTO ITEMS VALUES(?,?,?)"
cursor.execute(INSERT_ITEM,(1,"test",12.00))

connection.commit()
connection.close()