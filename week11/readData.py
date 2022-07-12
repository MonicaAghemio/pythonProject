from connect import *


def readFilms():
    cursor.execute("SELECT * FROM tblfilms")
    row = cursor.fetchall()
    for record in row:
        print(record)


# readFilms()
