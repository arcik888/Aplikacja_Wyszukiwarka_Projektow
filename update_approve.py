# -*- coding: utf-8 -*-

import db_connect as db
import datetime 
from fpdf import FPDF

cs = db.Conn().conn()
cur = cs.cursor()

#Pobranie z BD numerów projektów z statusem WIP
cur.execute("SELECT * FROM all_ki WHERE rev_status = 'WIP'")
print("Projekty oczekujące na akceptację: ")
for wip in cur:
    nr_ki = wip[1]
    rev = wip[2]
    print(nr_ki + rev)

# podaje status z BD
cur.execute("SELECT * FROM status WHERE stat_id = 2")
for app in cur:
    approve = app[1]
   
nr_ki = input('Który numer KI akceptujesz?: ')

if len(nr_ki) == 8:
    accept = input('Czy projekt jest ok? [T/N]: ')
    if accept.lower() == 't': #and check() == True:
        nr = nr_ki[:7]
        rev = nr_ki[-1]
        # aktualizacja statusu rewizji dla danego numeru projektu w bazie 
        cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s AND rev = %s" , (approve, nr, rev))
        # aktualna data
        dat = datetime.datetime.now().date()
        # aktualny czas
        tim = datetime.datetime.now().time()
        # wstawianie do bazy do tabeli historycznej
        cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
            VALUES (%s, %s, %s, %s, %s)", (nr, rev, approve, dat, tim))
        #zebranie z bazy ścieżki projektu
        cur.execute("SELECT * FROM all_ki WHERE nr_ki = %s" % ("'" + nr + "'"))
        for path in cur: 
            path = path[4]

                # OPIS GABARYTÓW PROJEKTU
        print('Podaj gabaryty zewnętrzne produktu:')
        l = int(input('L: '))
        w = int(input('W: '))
        h = int(input('H: '))
    
        #wstawia do bazy gabaryty projektu
        cur.execute("UPDATE all_ki SET lenght = %s, width = %s, height = %s WHERE nr_ki = %s AND rev = %s" , (l, w, h, nr, rev))


    elif accept.lower() != 't':
        print("Brak akceptacji")

    elif len(nr_ki) != 8:
        print("Nieprawidłowy numer KI")
else: print("Nieprawidłowy numer KI")

# def document():
# Tworzy nowy dokument PDF
doc = FPDF()
doc.add_page()
doc.set_font('Arial', '', 12)
doc.cell(25, 10, nr_ki)
doc.output(path+"\\"+nr+" rev "+rev+"\\"+nr_ki+"_doc.pdf", "F")

cs.commit()
cs.close()
