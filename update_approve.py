import psycopg2 as pg
import datetime 

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

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
accept = input('Czy projekt jest ok? [T/N]: ')

if accept.lower() == 't' and len(nr_ki) == 8:
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

elif accept.lower() != 't':
    print("Brak akceptacji")

elif len(nr_ki) != 8:
    print("Nieprawidłowy numer KI")

conn.commit()
conn.close()
