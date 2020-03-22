# -*- coding: utf-8 -*-

import datetime
import os
from searching import Search 
import db_connect as db
cs = db.Conn().conn()
cur = cs.cursor()

nr_ki = ''
while nr_ki == '':
    nr_ki = input("Który numer projektu ma mieć podniesioną rewizję? [Podaj numer lub Wyszukaj [F]: ")
    # Wstawić wyszukiwanie
    if nr_ki.lower() == 'f':
        search = Search()
        nr_ki = input("Który numer projektu ma mieć podniesioną rewizję? ")
        # Podany numer dostaje folder z nową rewizją
        # z bay wyciągnąć ścieżkę do folderu i dodać katalog z nową rev
    nr = nr_ki[:7]
    rev = nr_ki[7]

    # podaje status WIP z BD
cur.execute("SELECT stat_name FROM status WHERE stat_id = 1")
for wip in cur:
    wip = wip[0]

rev = ord(rev)

if rev > 64 and rev < 91:
    rev += 1
    new_rev = chr(rev)
else:
    print('Błąd. Za wysoka rewizja! Utwórz nowy projekt.')
    conn.close()
    
# aktualna data
dat = datetime.datetime.now().date()
# aktualny czas
tim = datetime.datetime.now().time()
# wstawianie do bazy do tabeli historycznej
cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
    VALUES (%s, %s, %s, %s, %s)", (nr, new_rev, wip, dat, tim))

# pobiera dane z bazy - ścieżkę, klienta, nazwę
cur.execute("SELECT ki_path, customer, project_name, project_owner FROM all_ki WHERE nr_ki = %s" % ("'" + nr + "'"))
for kit in cur:
    path = kit[0]
    customer = kit[1]
    name_project = kit[2]
    project_owner = kit[3]
# tworzenie nowego katalogu ścieżka do katalogu
os.mkdir(path + '\\' + nr + ' rev ' + new_rev)

# WSTAWIA PROJEKT z nowa rewizja DO TABELI all_ki z statusem wip
cur.execute("INSERT INTO all_ki (nr_ki, rev, rev_status, ki_path, customer, project_name, project_owner) \
    VALUES (%s, %s, %s, %s, %s, %s, %s)", (nr, new_rev, wip, path, customer, name_project, project_owner))

cs.commit()
cs.close()
