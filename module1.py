import psycopg2 as pg
from datetime import date

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

# Pobranie z BD numerów projektów z statusem APPROVED

cur.execute("SELECT * FROM nr_ki WHERE stat_rev_ki = 'APPROVED' ")
for record in cur:
    print(record[0])

nr_ki = input('Który numer KI uwalniasz do produkcji?: ')
accept = input('Czy projekt jest ok? [T/N]: ')

if accept == 't' or accept == 'T':
    cur.execute("UPDATE nr_ki SET stat_rev_ki = %s WHERE stat_rev_ki=%s AND nr_ki = %s" , ('RELEASED', 'APPROVED', nr_ki))

conn.commit()
conn.close()

