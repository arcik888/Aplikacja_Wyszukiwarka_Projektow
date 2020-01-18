# -*- coding: utf-8 -*-

import psycopg2 as pg
from project import Project 
import datetime 

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
    dat = datetime.datetime.now().date()
    tim = datetime.datetime.now().time()
    cur.execute("SELECT stat_name FROM status WHERE stat_id = 1")
    for record in cur:
        stat = record

    # OPIS PROJEKTU
    desc_path = path_ + '\\' + 'Opis.txt'
    desc_file = open(desc_path, 'w')
    description = desc_file.write(input("Opis projektu: "))
    desc_file.close()
    
    # WSTAWIA NOWY PROJEKT DO TABELI all_ki
    cur.execute("INSERT INTO all_ki (nr_ki, rev, rev_status, ki_path, customer, project_name) \
        VALUES (%s, %s, %s, %s, %s, %s)", (nr_ki, 'A', stat, path_, customer, name_project))

    # WSTAWIA DO TABELI hystory NOWY PROJEKT
    cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
        VALUES (%s, %s, %s, %s, %s)", (nr_ki, 'A', stat, dat, tim))

else:
    pass

conn.commit()
conn.close()