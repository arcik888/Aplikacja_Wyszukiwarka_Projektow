import psycopg2 as pg
import datetime 

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

#Pobranie z BD numerów projektów z statusem WIP
cur.execute("SELECT * FROM all_ki WHERE rev_status = 'APPROVED'")
print("Projekty oczekujące na uwolnienie do produkcji: ")
for app in cur:
    print(app[1])

# podaje status z BD
cur.execute("SELECT * FROM status WHERE stat_name = 'RELEASED'")
for rel in cur:
    release = rel[1]
   
nr_ki = input('Który numer KI uwalniasz?: ')
accept = input('Czy projekt jest ok? [T/N]: ')

if accept == 't' or accept == 'T':
    cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s" , (release, nr_ki))
    cur.execute("SELECT rev FROM all_ki WHERE nr_ki = %s ORDER BY nr_ki desc LIMIT 1" % ("'" + nr_ki + "'"))
    for rev in cur: rev
    dat = datetime.datetime.now().date()
    tim = datetime.datetime.now().time()
    cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
        VALUES (%s, %s, %s, %s, %s)", (nr_ki, rev, release, dat, tim))

conn.commit()
conn.close()