from connect import *
import readData
import time


def deleteFilm():
    idField = input("Enter filmID of the film to be deleted: ")
    cursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField}")
    conn.commit()
    print(f"Records {idField} deleted from table")

    time.sleep(3)
    readData.readFilms()


# deleteFilm()
