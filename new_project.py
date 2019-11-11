import psycopg2 as pg
from project import Project 

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
cur.execute("SELECT * FROM public.nr_ki ORDER BY ki_id DESC LIMIT 1")
for record in cur:
    id = record[0]
nr_ki = project.last_num[:7]
path_ = project.last_path + '\\' + project.last_num

id += 1

#if id == None:
#    id = 1
#else:
#    id = id + 1
    
cur.execute('INSERT INTO public.nr_ki (ki_id, ki_nr, ki_pathh) VALUES (%s, %s, %s)' , (id, nr_ki, path_))

conn.commit()
conn.close()