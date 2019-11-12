from project import Project
import psycopg2 as pg
from datetime import date

conn = pg.connect("dbname = Projects_test user = postgres password = Pa$$w0rd")
cur = conn.cursor()

#Sprawdzenie ststusu projektu w BD

cur.execute("SELECT * FROM public.ki_history WHERE status = 'WIP' ")
for record in cur:
    print(record)
    nr_ki = record[1]
    rev = record[2]

cur.execute("SELECT * FROM public.ki_history ORDER BY id DESC LIMIT 1")
for record in cur:
    id_ = record[0] + 1

accept = input('Czy projekt jest ok? [T/N]: ')
date_ = date.today()

if accept == 't' or accept == 'T':
    cur.execute("INSERT INTO ki_history (id,nr_ki,rev,status,date) VALUES (%s, %s, %s, %s, %s)" , (id_, nr_ki, rev, 'APPROVED', date_))




conn.commit()
conn.close()