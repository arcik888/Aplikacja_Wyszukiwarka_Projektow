import psycopg2 as pg
from datetime import date

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

# Pobranie z BD numerów projektów z statusem APPROVED

cur.execute("SELECT * FROM status")
for record in cur:
    print(record)

cur.execute("INSERT INTO all_ki (nr_ki, rev_ki, stat_rev_ki, ki_path, datetime, customer, project_name) VALUES (%s, %s, %s, %s, %s, %s, %s)", ('KI10293', 'A', 'WIP', 'C:\\', '2019-11-11', 'ABB', 'ABC'))

#SELECT id_ki, nr_ki, rev_ki, stat_rev_ki, ki_path, datetime, customer, project_name
#	FROM public.all_ki;

conn.commit()
#conn.close()

