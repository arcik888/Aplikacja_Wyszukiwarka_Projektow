# -*- coding: utf-8 -*-

import db_connect as db
import datetime 
from fpdf import FPDF

cs = db.Conn().conn()
cur = cs.cursor()

#Pobranie z BD numerów projektów z statusem WIP
cur.execute("SELECT * FROM all_ki WHERE rev_status = 'WIP'")
print("Projekty oczekujące na akceptację: ")

proj = []
for wip in cur:
    project = wip[1] + wip[2]
    proj.append(project)
for p in proj:
    print(p)

nr_ki = input('Który numer KI akceptujesz?: ')
if nr_ki in proj:
    accept = input('Czy projekt jest ok? [T/N]: ')
    if accept.lower() == 't': #and check() == True:
        nr = nr_ki[:7]
        rev = nr_ki[-1]
        # podaje status z BD
        cur.execute("SELECT * FROM status WHERE stat_id = 2")
        for app in cur:
            approve = app[1]
        # aktualna data
        dat = datetime.datetime.now().date()
        # aktualny czas
        tim = datetime.datetime.now().time()
        # OPIS GABARYTÓW PROJEKTU
        print('Podaj gabaryty zewnętrzne produktu:')
        l = int(input('L: '))
        w = int(input('W: '))
        h = int(input('H: '))
        #wstawia do bazy gabaryty projektu
        cur.execute("UPDATE all_ki SET rev_status = %s lenght = %s, width = %s, height = %s \
                     WHERE nr_ki = %s AND rev = %s" , (approve, l, w, h, nr, rev))
        # wstawianie do bazy do tabeli historycznej
        cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
            VALUES (%s, %s, %s, %s, %s)", (nr, rev, approve, dat, tim))
    elif accept.lower() != 't':
        print("Brak akceptacji")
else: print("Nieprawidłowy numer KI")

# Tworzy nowy dokument PDF
# zebranie z bazy ścieżki projektu

cur.execute("SELECT * FROM all_ki WHERE nr_ki = %s" % ("'" + nr + "'"))
for path in cur: 
    path = path[4]

doc = FPDF()
doc.add_page()
doc.set_font('Arial', '', 12)
doc.cell(25, 10, nr_ki)
doc.output(path+"\\"+nr+" rev "+rev+"\\"+nr_ki+"_doc.pdf", "F")

cs.commit()
cs.close()

