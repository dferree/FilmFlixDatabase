import sqlite3 as sql

dbCon = sql.connect("filmflix.db")

dbCursor = dbCon.cursor()
