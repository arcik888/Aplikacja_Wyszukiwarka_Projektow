import psycopg2 as pg
from datetime import date

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

#Pobranie z BD numerów projektów z statusem WIP

cur.execute("SELECT * FROM all_ki")
for record in cur:
    wip = record
    # WYŚWIETLA LISTĘ NUMERÓW, KTÓRE MAJĄ STATUS WIP
    if wip[3] == 'WIP':

        print(wip[1])
    # ALE NIE MAJĄ STATUSU APPROVED
    # JEŻELI TEN SAM NUMER MA STATUS WIP I APPROVED, NIE WYŚWIETLAJ


nr_ki = input('Który numer KI akceptujesz?: ')
accept = input('Czy projekt jest ok? [T/N]: ')

if accept == 't' or accept == 'T':
    nr_ki = ("'" + nr_ki + "'")
    cur.execute("SELECT rev_ki FROM all_ki WHERE all_ki.nr_ki = %s ORDER BY id_ki DESC LIMIT 1" % (nr_ki))
    for rev in cur: rev
    cur.execute("SELECT status FROM status WHERE id_status = 2")
    for stat in cur: stat
    cur.execute("SELECT ki_path FROM all_ki WHERE nr_ki = %s" % (nr_ki))
    for path_ in cur: path_
    dat = date.today()
    cur.execute("SELECT customer FROM all_ki WHERE nr_ki = %s" % (nr_ki))
    for cust in cur: cust
    cur.execute("SELECT project_name FROM all_ki WHERE nr_ki = %s" % (nr_ki))
    for name in cur: name
    tup = (nr_ki, rev, stat, path_, dat, cust, name)
    #cur.execute("INSERT INTO all_ki (nr_ki, rev_ki, stat_rev_ki, ki_path, datetime, customer, project_name) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nr_ki, rev, stat, path_, dat, cust, name))
    
conn.commit()
conn.close()