from connect import *



def deleteFilm():
    #Use primary key to delete a record
    idField = input("Enter the FilmID of the film to be deleted: ")

    confirmDelete = input(f"Are you sure you want to delete the film {idField}?  Y/N  ")
    if confirmDelete == "Y":
        dbCursor.execute(f"DELETE FROM films WHERE FilmID = {idField}")
        dbCon.commit()
        print(f"Film {idField} deleted from the films table")
    else:
        print("Deletion aborted!")

if __name__ == "__main__":
    deleteFilm()
