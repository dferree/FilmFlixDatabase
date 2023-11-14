from connect import *
import readFilms

def updateFilm():
    readFilms.readData()

    idField = input("Enter the FilmID of the film to be updated: ")

    titleField = input("Enter film title: ")
    yearReleasedField = int(input("Enter release year: "))
    ratingField = input("Enter the rating: ")
    durationField = int(input("Enter the duration of the film: "))
    genreField = input("Enter the genre of the film: ")

    # Add single quotes on the values to be updated
    titleField = "'"+titleField+"'"
    ratingField = "'"+ratingField+"'"
    genreField = "'"+genreField+"'"


    # update a field in a record
    dbCursor.execute(f"UPDATE films SET Title = {titleField}, yearReleased = {yearReleasedField}, Rating = {ratingField}, Duration = {durationField}, Genre = {genreField} WHERE filmID = {idField}")
    dbCon.commit()
    print(f"Record {idField}  updated in the films table")

if __name__ == "__main__":
    updateFilm()
