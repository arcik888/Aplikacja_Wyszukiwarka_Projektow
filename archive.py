# -*- coding: utf-8 -*-

import datetime
from searching import Search 
import db_connect as db
cs = db.Conn().conn()
cur = cs.cursor()

nr_ki = ''
while nr_ki == '':
    nr_ki = input("Który numer projektu wychodzi z produkcji? [Podaj numer lub Wyszukaj [F]: ")
    if nr_ki.lower() == 'f':
        search = Search()
        nr_ki = input("Który numer projektu wychodzi z produkcji?")
        # 
    nr = nr_ki[:7]
    rev = nr_ki[7]

# pobiera status ARCHIVED z bazy
cur.execute("SELECT stat_name FROM status WHERE stat_id = 4")
for arch in cur:
    arch = arch[0]

# aktualna data
dat = datetime.datetime.now().date()
# aktualny czas
tim = datetime.datetime.now().time()

# wstawianie do bazy do tabeli historycznej
cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
    VALUES (%s, %s, %s, %s, %s)", (nr, rev, arch, dat, tim))

# aktualizuje status do ARCHIVED w podanym numerze KI
cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s AND rev = %s" , (arch, nr, rev))

cs.commit()
cs.close()
