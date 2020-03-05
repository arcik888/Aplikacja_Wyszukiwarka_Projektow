# -*- coding: utf-8 -*-
from login import Logging
import getpass

log = False
while log != True:
    login = input("Login: ")
    passwd = getpass.getpass("Hasło: ")
    loger = Logging(login, passwd)
    log = loger.logging()
    master = loger.master()

choice = ""
while choice.lower() != "exit":

    print("Wybierz co chcesz zrobić:")
    print("- Utwórz nowy projekt [N]: ")
    if master == True:
        print("- Akceptuj projekt [A]:")
    print("- Uwolnij projekt do produkcji [R]:")
    print("- Zmień rewizję [I]:")
    print("- Wyszukaj projekt [F]:")
    print("lub 'exit' aby zakończyć.")
    choice = input()

    if choice.lower() == "n":
        import new_project
    elif choice.lower() == "a":
        import update_approve
    elif choice.lower() == "r":
        import update_release
    elif choice.lower() == "i":
        import change_rev
    elif choice.lower() == "f":
        import searching
        search = searching.Search()
        search
        