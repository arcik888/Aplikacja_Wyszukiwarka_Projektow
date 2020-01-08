import psycopg2 as pg
import datetime
import os
from searching import Search 

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()


nr_ki = ''
while nr_ki == '':
    nr_ki = input("Który numer projektu ma mieć zmienioną rewizję? [Podaj numer lub Wyszukaj [F]: ")
    # Wstawić wyszukiwanie
    if nr_ki.lower() == 'f':
        search = Search()
        nr_ki = input("Który numer projektu ma mieć zmienioną rewizję? ")
        # Podany numer dostaje folder z nową rewizją
        # z bay wyciągnąć ścieżkę do folderu i dodać katalog z nową rev
    nr = nr_ki[:7]
    rev = nr_ki[7]

    # podaje status z BD
cur.execute("SELECT * FROM status WHERE stat_id = 1")
for wip in cur:
    wip = wip[1]

# wybrać z bazy aktualną rewizję dla projektu
#cur.execute("SELECT rev FROM all_ki WHERE nr_ki = %s" % ("'" + nr + "'"))
#for rev in cur: rev
#rev = rev[2] # dalej podnieść literę rewizji
rev = ord(rev)

if rev > 64 and rev < 91:
    rev += 1
    new_rev = chr(rev)
else:
    print('Błąd. Za wysoka rewizja!')
    conn.close()
    
# aktualna data
dat = datetime.datetime.now().date()
# aktualny czas
tim = datetime.datetime.now().time()
# wstawianie do bazy do tabeli historycznej
cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
    VALUES (%s, %s, %s, %s, %s)", (nr, new_rev, wip, dat, tim))

# pobiera dane z bazy - ścieżkę, klienta, nazwę
cur.execute("SELECT ki_path, customer, project_name FROM all_ki WHERE nr_ki = %s" % ("'" + nr + "'"))
for kit in cur:
    path = kit[0]
    customer = kit[1]
    name_project = kit[2]
# tworzenie nowego katalogu ścieżka do katalogu
os.mkdir(path + '\\' + nr + ' rev ' + new_rev)

# WSTAWIA PROJEKT z nowa rewizja DO TABELI all_ki z statusem wip
cur.execute("INSERT INTO all_ki (nr_ki, rev, rev_status, ki_path, customer, project_name) \
    VALUES (%s, %s, %s, %s, %s, %s)", (nr, new_rev, wip, path, customer, name_project))

conn.commit()
conn.close()

    # stworzyć nowy katalogn nowej rewizji


    # PLIK ECO MÓWIĄCY DLACZEGO I KIEDY ZOSTAŁ ZMIENIONY PROJEKT
    # PLIK MA ZAWIERAĆ: data, numer KI, opis dlaczego został zmieniony, numer zmiany, kto zmienił
    # zmiana BOMu do tego ECO


    # przy zmianie rev odczytać z bazy ostatnią rewizję projektu
    # wstawić wyższą rewizję o 1
    # rewizja jest w statusie WIP