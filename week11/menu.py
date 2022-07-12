import readData
import createData
import updateData
import search
import deleteData


def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5", "6"]:
        print("Songs Menu options:\nEnter \n1. To print.\n2. To add.\n3. To update.\n4. To delete.\n5. Search\n6. Exit")
        # reassign the options variable with a different value
        options = input("\nEnter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice")
    return options


# create a boolean flag variable and set it to True
mainProgram = True

while mainProgram == True:
    mainMenu = menuOptions()  # we assigned the menuOptions() to a variable
    # in options = 1/2/3/4/5 we can call the respective app and it subroutine
    if mainMenu == "1":
        readData.readFilms()
    elif mainMenu == "2":
        createData.addFilm()
    elif mainMenu == "3":
        updateData.updateFilms()
    elif mainMenu == "4":
        deleteData.deleteFilm()
    elif mainMenu == "5":
        search.searchF()
    else:
        mainProgram = False
input("press Enter to exit ")

menuOptions()
