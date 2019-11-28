import psycopg2 as pg
import datetime 
import os

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

#Pobranie z BD numerów projektów z statusem WIP
cur.execute("SELECT * FROM all_ki WHERE rev_status = 'WIP'")
print("Projekty oczekujące na akceptację: ")
for wip in cur:
    print(wip[1])

# podaje status z BD
cur.execute("SELECT * FROM status WHERE stat_name = 'APPROVED'")
for app in cur:
    approve = app[1]
   
nr_ki = input('Który numer KI akceptujesz?: ')
accept = input('Czy projekt jest ok? [T/N]: ')

if accept == 't' or accept == 'T':
    cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s" , (approve, nr_ki))
    cur.execute("SELECT rev FROM all_ki WHERE nr_ki = %s ORDER BY nr_ki desc LIMIT 1" % ("'" + nr_ki + "'"))
    for rev in cur: rev[0]
    dat = datetime.datetime.now().date()
    tim = datetime.datetime.now().time()
    cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
        VALUES (%s, %s, %s, %s, %s)", (nr_ki, rev, approve, dat, tim))

    cur.execute("SELECT ki_path FROM all_ki WHERE nr_ki = %s" % ("'" + nr_ki + "'"))
    for path in cur: path
    all_rev = os.listdir(path[0])
    for i in all_rev:
        if i[-1] == rev[0]:
            rev_path = path[0] + '\\' + i

    bom_file = rev_path + '\\' + 'BOM.txt'
    file = open(bom_file, 'w')
    files = os.listdir(rev_path)
    for f in files:
        if f != 'BOM.txt':
            file.write(f + '\n')
    file.close()

    os.listdir(rev_path)

conn.commit()
conn.close()