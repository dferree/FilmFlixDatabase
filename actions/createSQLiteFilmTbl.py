from connect import *

dbCursor.execute("""
CREATE TABLE "films" (
	"filmID"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"YearReleased"	INTEGER,
    "Rating" TEXT,
	"Duration"	INTEGER,
    "Genre" TEXT,
	PRIMARY KEY("filmID" AUTOINCREMENT)
)""")
