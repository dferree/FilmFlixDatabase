import textFiles, addFilms, deleteFilms, updateFilms, readFilms, reports

def mainMenu():
    options = 0
    optionsList = ["1","2","3"]
    # call/invoke our menu files function
    userChoices = textFiles.menuFiles()
    while options not in optionsList:
        print(userChoices[0])
        options  = input("Enter an option from the main menu above: ")
        if options not in optionsList:
            print(f"{options} is not a valid choice in the main menu! ")
    return options

# function for films menu
def filmsSubMenu():
    options = 0
    optionsList = ["1","2","3","4","5"]
    userChoices = textFiles.menuFiles()
    while options not in optionsList:
        print(userChoices[1]) #userMainMenu
        options  = input("Enter an option from the films menu above: ")
        if options not in optionsList:
            print(f"{options} is not a valid choice in the films menu! ")
    return options

# function for reports menu
def reportSubMenu():
    options = 0
    optionsList = ["1","2","3","4","5"]
    userChoices = textFiles.menuFiles()

    while options not in optionsList:
        print(userChoices[2]) #userSubMenu
        options  = input("Enter an option from the reports sub menu above: ")

        if options not in optionsList:
            print(f"{options} is not a valid choice in the reports sub menu! ")
    return options

#Main program: call the songs menu function and the report sub menu function
mainProgram = True
while mainProgram: # while True
    userChoice = mainMenu()
    if userChoice == "1":
        filmProgram = True
        while filmProgram:
            filmMenu = filmsSubMenu()
            if filmMenu == "1":
                readFilms.readData()
            elif filmMenu =="2":
                addFilms.insertFilms()
            elif filmMenu == "3":
                updateFilms.updateFilm()
            elif filmMenu == "4":
                deleteFilms.deleteFilm()
            else:
                filmProgram = False
                input("Press enter to return to the Main Menu")

    elif userChoice == "2":
        reportProgram = True
        while reportProgram:
            reportMenu = reportSubMenu()
            if reportMenu == "1":
                reports.getReports()
            elif reportMenu == "2":
                reports.searchGenre()
            elif reportMenu == "3":
                reports.searchYear()
            elif reportMenu == "4":
                reports.searchRating()
            else:
                reportProgram = False
                input("Press enter to return to the Main Menu")

    else:
        mainProgram = False
        input("Press enter to exit the program")
