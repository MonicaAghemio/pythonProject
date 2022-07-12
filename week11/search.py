from connect import *
import time


def searchFilm():
    Options = 0

    global details

    while Options not in ["1", "2", "3", "4", "5"]:
        print("Enter which data you would like to print:\n1. All films\n2. Particular genre\n3. Particular year\n4. Particular rating\n5. Exit ")
        Options = input("\nEnter one of the options above: ")
    if Options in ["1", "2", "4"]:
        details = input(
            "Enter description (if option 1, just press Enter): ")
    elif Options in ["3"]:
        details = input("Enter year: ")
        convertedDetails = str(details)
    else:
        print("Exit")

    return Options


mainProg = True
while mainProg == True:
    mainMenu = searchFilm()
    if mainMenu == "1":
        cursor.execute("SELECT * FROM tblfilms")
    elif mainMenu == "2":
        cursor.execute("SELECT * FROM tblfilms WHERE genre =" +
                       "'" + details + "'")
    elif mainMenu == "3":
        cursor.execute(
            "SELECT * FROM tblfilms WHERE yearReleased =" + details)
    elif mainMenu == "4":
        cursor.execute(
            "SELECT * FROM tblfilms WHERE rating =" + "'" + details + "'")
    else:
        mainProg = False

conn.commit()
time.sleep(3)

row = cursor.fetchall()
strRow = str(row)
if details in strRow:
    for record in row:
        print(record)
else:
    print(
        f"field does not contain a {details} in the database")

input("press Enter to exit ")


# searchFilm()
