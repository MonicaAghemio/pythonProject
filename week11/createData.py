from connect import *
import time


def addFilm():
    filmID = []
    title = input("Enter film title: ")
    year = int(input("Released year: "))
    rating = input("Rating: ")
    duration = int(input("Duration: "))
    genre = input("Genre: ")

    filmID.append(title)
    filmID.append(year)
    filmID.append(rating)
    filmID.append(duration)
    filmID.append(genre)

    cursor.execute("INSERT INTO tblfilms VALUES(NULL, ?, ?, ?, ?, ?)", filmID)
    conn.commit()
    print(f"{title} added to table")
    time.sleep(3)

    cursor.execute("SELCT * FROM filmID")
    row = cursor.fetchall()
    for record in row:
        print(record)


# addFilm()
