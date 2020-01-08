import psycopg2 as pg
import os

conn = pg.connect("dbname = projects user = postgres password = Pa$$w0rd")
cur = conn.cursor()
class Search:
    def __init__(self):
        def find_phrase():
            # ZNAJDOWANIE PO OPISIE Z PLIKU TEKSTOWEGO
            fraza = input('Podaj szukaną frazę: ')
            fraza.lower()
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
                                        f = data.lower().find(fraza)
                                    if f > -1: print(l[:7])

        def find_lenght():                        
            # ZNAJDOWANIE PO L
            to_find = input("Podaj szukaną długość 'L'[mm]:")
            cur.execute("SELECT nr_ki, rev, lenght FROM all_ki")
            for lenght in cur: 
                lenght
                if lenght[2] == int(to_find): print(lenght[0], lenght[1])

        def find_width():
            # ZNAJDOWANIE PO W
            to_find = input("Podaj szukaną szerokość 'W'[mm]:")
            cur.execute("SELECT nr_ki, rev, width FROM all_ki")
            for width in cur: 
                width
                if width[2] == int(to_find): print(width[0], width[1])

        def find_height():
        # ZNAJDOWANIE PO H
            to_find = input("Podaj szukaną wysokość 'H'[mm]:")
            cur.execute("SELECT nr_ki, rev, height FROM all_ki")
            for height in cur: 
                height
                if height[2] == int(to_find): print(height[0], height[1])

        def find_customer():
        # ZNAJDOWANIE PO KLIENCIE
            to_find = input("Podaj nazwę klienta:")
            cur.execute("SELECT nr_ki, rev, customer FROM all_ki")
            for customer in cur: 
                customer
                if customer[2].lower() == to_find.lower(): print(customer[0], customer[1])

        def find_projectname():
        # ZNAJDOWANIE PO NAZWIE PROJEKTU
            to_find = input("Podaj nazawę projektu:")
            cur.execute("SELECT nr_ki, rev, project_name FROM all_ki")
            for name in cur: 
                name
                data = name[2].lower()
                data = data.find(to_find.lower())
                if data > -1: print(name[0], name[1])

        def find_rev():
            to_find = input("Podaj numer projektu:")
            cur.execute("SELECT nr_ki, rev, rev_status FROM all_ki")
            for ki in cur: 
                ki
                if to_find[:7] == ki[0]: print(ki[0] + ' - rev: ' + ki[1] + ' - status: ' + ki[2])

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
            - Sprawdź aktualną rewizję ['R']:
            lub 'exit' aby zakończyć.
            """)

            if search.upper() == 'O':
                find_phrase()
            elif search.upper() == 'L':
                find_lenght()
            elif search.upper() == 'W':
                find_width()
            elif search.upper() == 'H':
                find_height()
            elif search.upper() == 'C':
                find_customer()
            elif search.upper() == 'N':
                find_projectname()
            elif search.upper() == 'R':
                find_rev()
            else:
                "Wystąpił błąd!"
