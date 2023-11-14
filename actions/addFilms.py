from connect import *

def insertFilms():
   title = input("Enter film title: ")
   yearReleased = input("Enter release year: ")
   rating = input("Enter the rating: ")
   duration = input("Enter the duration of the film: ")
   genre = input("Enter the genre of the film: ")

   dbCursor.execute("INSERT INTO films (Title, yearReleased, Rating, Duration, Genre) VALUES (?,?,?,?,?)", (title, yearReleased, rating, duration, genre))
   dbCon.commit()

   print(f"{title} has been added to the films table.")

if __name__ == "__main__":
    insertFilms()
