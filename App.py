# -*- coding: utf-8 -*-
from login import Logging
import getpass
import os
import json
import db_connect as db
cs = db.Conn().conn()
cur = cs.cursor()

log = False
while log != True:
    login = input("Login: ")
    passwd = getpass.getpass("Hasło: ")
    loger = Logging(login, passwd)
    log = loger.logging()

    cur.execute("SELECT * FROM designers WHERE login = %s" % ("'"+login+"'"))
    for info in cur: info
    info = {'f_name': info[1], 'l_name':info[2], 'master': info[3]}
    with open('C:\\Users\\Public\\Temp.json', 'w') as js:
        json.dump(info, js)

choice = ""
while choice.lower() != "exit":

    print("Wybierz co chcesz zrobić:")
    print("- Utwórz nowy projekt [N]: ")
    if info['master'] == True:
        print("- Akceptuj projekt [A]:")
    print("- Uwolnij projekt do produkcji [R]:")
    print("- Zmień rewizję [I]:")
    print("- Wycofaj z produkcji [W]:")
    print("- Wyszukaj projekt [F]:")
    print("lub 'exit' aby zakończyć.")
    choice = input()

    if choice.lower() == "n":
        import new_project
    elif choice.lower() == "a" and info['master'] == True:
        import update_approve
    elif choice.lower() == "r":
        import update_release
    elif choice.lower() == "i":
        import change_rev
    elif choice.lower() == "f":
        import searching
        search = searching.Search()
        search
    elif choice.lower() == "w":
        import archive
    elif choice.lower() == "exit":
        if os.path.isfile('C:\\Users\\Public\\Temp.json'):
            os.remove('C:\\Users\\Public\\Temp.json')