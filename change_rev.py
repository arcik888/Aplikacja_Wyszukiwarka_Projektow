import os
from project import Project
import psycopg2 as pg

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()
cur.execute("SELECT * FROM public.nr_ki")
to_find = 'KI32966'
for record in cur:
    id = record[0]
    ki_num = record[1]
    ki_path = record[2]
    if ki_num == to_find:
        print(ki_num)


top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'

project = Project(top_path, 'Syncreon', 'KI32938')

#os.mkdir(project.last_project()[3][:7] + '\\' + project.last_project()[3][:7] + "new rev")

