import psycopg2 as pg

conn = pg.connect("dbname = Projects_test user = postgres password = Pa$$w0rd")

cur = conn.cursor()

cur.execute("CREATE TABLE test (id int PRIMARY KEY,  name varchar);")



conn.commit()
conn.close()