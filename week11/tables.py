from connect import *

cursor.execute("""

CREATE TABLE "tblfilms" (
	"filmID"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT,
	"yearReleased"	INTEGER NOT NULL,
	"rating"	TEXT,
    "duration" INTEGER NOT NULL,
    "genre" TEXT,
	PRIMARY KEY("filmID" AUTOINCREMENT)
)"""
