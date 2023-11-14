from connect import *


def readData():
    dbCursor.execute("SELECT * FROM films")

    allFilms = dbCursor.fetchall()
    #loop through all records held as a list in the allRecords variable
    for film in allFilms:
        # display each record
        print(film)


if __name__ == "__main__":
    readData()
