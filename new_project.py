# -*- coding: utf-8 -*-

import db_connect as db
import datetime
import os
import json
from project import Project
import socket
import pickle

IP = '192.168.13.6'
port = 34543
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, port))
s.listen(4)
while True:
    clientsocket , address = s.accept()
    print(f"Połączenie przychodzące z {address}")
    clientsocket.send(bytes("Witaj w Aplikacji.", "UTF-8"))

cs = db.Conn().conn()
cur = cs.cursor()

new_project = clientsocket.send(bytes("Czy chcesz utworzyć nowy projekt? [T/N]: ", "UTF-8"))

if new_project == 'T' or new_project == 't':
    top_path = 'C:\\Firma\\DESIGNS\\'
    customer = clientsocket.send(bytes("Klient: ", "UTF-8"))
    name_project = clientsocket.send(bytes("Nazwa projektu: ", "UTF-8"))
    project = Project(top_path, customer.capitalize(), name_project.upper())
    project.new_project()
    nr_ki = project.last_num[:7]
    path_ = project.last_path + '\\' + project.last_num
    dat = datetime.datetime.now().date()
    tim = datetime.datetime.now().time()
    cur.execute("SELECT stat_name FROM status WHERE stat_id = 1")
    for record in cur:
        stat = record

    # OPIS PROJEKTU
    with open(path_ + '\\' + 'Opis.txt', 'w') as desc:
        desc.write(input("Opis projektu: "))

    # POBIERANIE NAZWISKA PROJEKTANTA
    with open('C:\\Users\\Public\\Temp.json', 'r') as js:
        info = json.load(js)
        designer_name = info['f_name'] + " " + info['l_name']

    # WSTAWIA NOWY PROJEKT DO TABELI all_ki
    cur.execute("INSERT INTO all_ki (nr_ki, rev, rev_status, ki_path, customer, project_name, project_owner) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)", (nr_ki, 'A', stat, path_, customer, name_project, designer_name))

    # WSTAWIA DO TABELI hystory NOWY PROJEKT
    cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
        VALUES (%s, %s, %s, %s, %s)", (nr_ki, 'A', stat, dat, tim))

else:
    pass

cs.commit()
cs.close()