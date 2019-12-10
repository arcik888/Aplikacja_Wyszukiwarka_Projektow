import psycopg2 as pg
import os

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()

def find_phrase():
    # ZNAJDOWANIE PO OPISIE Z PLIKU TEKSTOWEGO
    fraza = input('Podaj szukaną frazę: ')
    top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
    l0 = os.listdir(top_path)
    l1 = []
    for i in l0:    # petla szukajaca plikw opisowwych 
        if i[:2] == 'KI':
            p1 = top_path + i
            l1.append(p1)
            for j in l1:
                l2 = os.listdir(j)
            for k in l2:
                p2 = j + '\\' + k
                l2 = os.listdir(p2)
                for l in l2:
                    p3 = p2 + '\\' + l
                    l3 = os.listdir(p3)
                    for m in l3:
                        if m == "Opis.txt":
                            # zdefiniować sciezke pliku
                            m = p3 + '\\' + m
                            with open(m, 'r') as desc_file:
                                data = desc_file.read()
                                f = data.find(fraza)
                            if f > -1:
                                print(l)

def find_lenght():                        
    # ZNAJDOWANIE PO L
    to_find = input("Podaj szukaną długość 'L'[mm]:")
    cur.execute("SELECT nr_ki, lenght FROM all_ki")
    for lenght in cur: 
        lenght
        if lenght[1] == int(to_find):
            print(lenght[0])

def find_width():
    # ZNAJDOWANIE PO L
    to_find = input("Podaj szukaną szerokość 'W'[mm]:")
    cur.execute("SELECT nr_ki, width FROM all_ki")
    for width in cur: 
        width
        if width[1] == int(to_find):
            print(width[0])

def find_height():
# ZNAJDOWANIE PO H
    to_find = input("Podaj szukaną wysokość 'H'[mm]:")
    cur.execute("SELECT nr_ki, height FROM all_ki")
    for height in cur: 
        height
        if height[1] == int(to_find):
            print(height[0])

def find_customer():
# ZNAJDOWANIE PO KLIENCIE
    to_find = input("Podaj nazwę klienta:")
    cur.execute("SELECT nr_ki, customer FROM all_ki")
    for customer in cur: 
        customer
        if customer[1] == to_find:
            print(customer[0])

def find_projectname():
# ZNAJDOWANIE PO NAZWIE PROJEKTU
    to_find = input("Podaj nazawę projektu:")
    cur.execute("SELECT nr_ki, project_name FROM all_ki")
    for name in cur: 
        name
        data = name[1]
        data = data.find(to_find)
        if data > -1:
            print(name[0])

search = ''
while search != 'exit':
    search = input("""
    Wyszukiwanie (Wpisz odpowiedni znak):
    - Opis ['O']: 
    - Długość ['L']: 
    - Szerokość ['W']: 
    - Wysokość ['H']:
    - Klient ['C']:
    - Nazwa Projektu ['N']: 
    lub 'exit' aby zakończyć.
    """)

    if search == 'O':
        find_phrase()
    elif search == 'L':
        find_lenght()
    elif search == 'W':
        find_width()
    elif search == 'H':
        find_height()
    elif search == 'C':
        find_customer()
    elif search == 'N':
        find_projectname()
    else:
        "Wystąpił błąd!"

