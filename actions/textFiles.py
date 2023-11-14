def menuFiles():
    with open("mainMenu.txt")  as mainMenu:
        userMainMenu = mainMenu.read()

    with open("filmsMenu.txt") as filmsMenu:
        userFilmsMenu = filmsMenu.read()

    with open("reportsMenu.txt") as reportsMenu:
        userReportsMenu = reportsMenu.read()

    return userMainMenu, userFilmsMenu, userReportsMenu
