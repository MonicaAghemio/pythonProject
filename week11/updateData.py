from connect import *
import readData
import time


def updateFilms():
    idField = input("Enter the filmID of the film you want to update: ")
    fieldName = input(
        "Which field would you like to update (title, reliased year, rating, duration, genre)? ")
    newField = input(f"Enter new value for {fieldName}: ")
    print(f"New value entered is {newField}.")

    newField = " ' " + newField + " ' "
    print(f"new value: {newField}")
    cursor.execute(
        f"UPDATE tblfilms SET {fieldName} = {newField} WHERE filmID = {idField}")

    conn.commit()
    print(f"Record {idField} updated")


# updateFilms()
