import psycopg2 as pg
from new_project import Project 

conn = pg.connect("dbname = Projects_test user = postgres password = Pa$$w0rd")

top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'

new_project = input("Czy chcesz utworzyć nowy projekt? [T/N]: ")

customer = input("Klient: ")

name_project = input('Nazwa projektu: ')

project = Project(top_path, customer, name_project)

if new_project == 'T' or new_project == 't':
    project.new_project()
else:
    pass

cur = conn.cursor()

path = project.last_project.last_num
print(path)
#id = cur.execute("SELECT max (id) FROM Projects_test.nr_ki")

#cur.execute("INSERT INTO Projects_test.nr_ki VALUES (id, nr_ki, path)")

conn.commit()
conn.close()