from connect import *

def getReports():
    dbCursor.execute("SELECT * FROM films ORDER BY filmID DESC")
    filmData = dbCursor.fetchall()

    #loop through all records held as a list in the allRecords variable
    for film in filmData:
        # display each record
        print(film)

def searchGenre():
    genreSearch = str(input("Which genre do you want to search for: "))
    dbCursor.execute("SELECT * FROM films WHERE genre LIKE ?", ('%' + genreSearch + '%',))
    searchFilms = dbCursor.fetchall()

    if not searchFilms:
        print(f"No films in genre {genreSearch} found. Please search for another one")
    else:
        for film in searchFilms:
            print(film)

def searchYear():
    yearSearch = int(input("Which release year do you want to search for: "))
    dbCursor.execute("SELECT * FROM films WHERE yearReleased = ?", (yearSearch,))
    searchData = dbCursor.fetchall()

    if not searchData:
        print(f"No films in Year {yearSearch} found. Please search for another one.")
    else:
        for records in searchData:
            print(records)

def searchRating():
    ratingSearch = input("Which rating do you want to search for: ")
    dbCursor.execute("SELECT * FROM films WHERE rating LIKE ?", ('%' + ratingSearch + '%',))
    searchData = dbCursor.fetchall()

    if not searchData:
        print(f"No films in rating {ratingSearch} found. Please search for another one.")
    else:
        for records in searchData:
            print(records)

if __name__ == "__main__":
    getReports()
    searchGenre()
    searchYear()
    searchRating()
