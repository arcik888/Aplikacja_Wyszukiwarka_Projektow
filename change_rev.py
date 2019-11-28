import psycopg2 as pg

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

# WYSZUKANIE PROJEKTU
# - PO KLIENCIE
# - PO PROJEKCIE
# - PO NUMERZE
# - PO SŁOWACH KLUCZOWYCH W PLIKU OPISU
# - PO GABARYTACH


nr_ki = input("Który numer projektu ma mieć zmienioną rewizję?: ")

cur.execute("SELECT * FROM all_ki WHERE nr_ki = %s" % ("'" + nr_ki + "'"))

