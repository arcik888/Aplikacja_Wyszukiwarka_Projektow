import psycopg2 as pg
from project import Project 
from datetime import date

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

new_project = input("Czy chcesz utworzyć nowy projekt? [T/N]: ")

if new_project == 'T' or new_project == 't':
    top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
    customer = input("Klient: ")
    name_project = input('Nazwa projektu: ')
    project = Project(top_path, customer, name_project)
    project.new_project()
    nr_ki = project.last_num[:7]
    path_ = project.last_path + '\\' + project.last_num
    dat = date.today()
    cur.execute("SELECT status FROM status WHERE id_status = 1")
    for record in cur:
        stat = record
    #cur.execute('INSERT INTO nr_ki (nr_ki, rev_ki, stat_rev_ki, path_ki, customers, project_name) VALUES (%s, %s, %s, %s, %s, %s)' , (nr_ki, 'A', '', path_, customer, name_project))
    cur.execute("INSERT INTO all_ki (nr_ki, rev_ki, stat_rev_ki, ki_path, datetime, customer, project_name) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nr_ki, 'A', stat, path_, dat, customer, name_project))

else:
    pass

conn.commit()
conn.close()