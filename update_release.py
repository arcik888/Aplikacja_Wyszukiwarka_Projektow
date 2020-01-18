# -*- coding: utf-8 -*-

import psycopg2 as pg
import datetime 
import os

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

#Pobranie z BD numerów projektów z statusem APPROVED
cur.execute("SELECT * FROM all_ki WHERE rev_status = 'APPROVED'")
print("Projekty oczekujące na uwolnienie do produkcji: ")
for app in cur:
    print(app[1]+app[2])
   
nr_ki = input('Który numer KI jest zwolniony do produkcji?: ')
accept = input('Czy projekt jest ok? [T/N]: ')

if accept == 't' or accept == 'T' and nr_ki == 8:
    dat = datetime.datetime.now().date()
    tim = datetime.datetime.now().time()
    nr = nr_ki[:7]
    rev = nr_ki[-1]

    # jeżeli rewizja projektu jest wyższa niż A to poprzednia dostaje status ARCHIVED
    if ord(rev) > 65 and ord(rev) < 91:
        prev_rev = chr(ord(rev)-1) # poprzednia litera od podanej
        # pobiera z BD status ARCHIVED
        cur.execute("SELECT stat_name FROM status WHERE stat_id = 4")
        for arch in cur:
            arch = arch[0]
        cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s AND rev = %s" , (arch, nr, prev_rev))
        cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
        VALUES (%s, %s, %s, %s, %s)", (nr, prev_rev, arch, dat, tim))

    cur.execute("SELECT stat_name FROM status WHERE stat_id = 3")
    for rel in cur:
        rel = rel[0]
    cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s AND rev = %s" , (rel, nr, rev))

    cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
        VALUES (%s, %s, %s, %s, %s)", (nr, rev, rel, dat, tim))

    # wybiera ścieżke katalogu projektu
    cur.execute("SELECT ki_path FROM all_ki WHERE nr_ki = %s and rev = %s" % ("'" + nr + "'", "'" + rev + "'"))
    for path in cur: path
    #podaje ścieżkę ostatniej rewizji produktu
    all_rev = os.listdir(path[0])
    for i in all_rev:
        if i[-1] == rev:
            rev_path = path[0] + '\\' + i
    # tworzenie nowego pliku BOM dla reewizji
    bom_file = rev_path + '\\' + 'BOM.txt'
    file = open(bom_file, 'w')
    files = os.listdir(rev_path)
    for f in files:
        if f != 'BOM.txt' and f[0] != 'F' and f[-4:] == '.pdf':
            file.write(f[:-4] + '\n')
    file.close()
    
    # OPIS GABARYTÓW PROJEKTU
    print('Podaj gabaryty produktu:')
    l = int(input('L: '))
    w = int(input('W: '))
    h = int(input('H: '))
    
    #wstawia do bazy gabaryty projektu
    cur.execute("UPDATE all_ki SET lenght = %s, width = %s, height = %s WHERE nr_ki = %s AND rev = %s" , (l, w, h, nr, rev))

elif accept.lower() != 't':
    print("Brak akceptacji")

elif len(nr_ki) != 8:
    print("Nieprawidłowy numer KI")

conn.commit()
conn.close()

# automatyczne dodawanie wykrojników
# przypisywanie pian do BOMów?
# uzupełnienie informacji do dokumentacji
# wprowadzenie właściciela projekltu (logowanie)
# zaczęcie wprowadzenia potrzebnych dokumentów

# w bomie uzupełnienie paletyzacji
# paletyzacja półproduktów i FG

