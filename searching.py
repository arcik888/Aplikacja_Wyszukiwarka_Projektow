# -*- coding: utf-8 -*-

import os
import db_connect as db

cs = db.Conn().conn()
cur = cs.cursor()

class Search:
    def __init__(self, condition):
        self.condition = condition
    def find_phrase(self):
        # ZNAJDOWANIE PO OPISIE Z PLIKU TEKSTOWEGO
        fraza = self.condition
        fraza.lower()
        top_path = 'C:\\Firma\\DESIGNS\\'
        l0 = os.listdir(top_path)
        l1 = []
        result = []
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
                                m = p3 + '\\' + m
                                with open(m, 'r') as desc_file:
                                    data = desc_file.read()
                                    f = data.lower().find(fraza)
                                    if f > -1: 
                                        num = l3[0][:7]
                                        result.append(num)
            return result

    def find_lenght(self):                        
        # ZNAJDOWANIE PO L
        to_find = self.condition
        result = []
        cur.execute("SELECT nr_ki, rev, lenght FROM all_ki")
        for lenght in cur: 
            lenght
            if lenght[2] == int(to_find): 
                result.append(lenght[0]+lenght[1])
        return result

    def find_width(self):
        # ZNAJDOWANIE PO W
        to_find = self.condition
        result = []
        cur.execute("SELECT nr_ki, rev, width FROM all_ki")
        for width in cur: 
            width
            if to_find and width[2] == int(to_find):
                result.append(width[0] + width[1])
        return (result)

    def find_height(self):
    # ZNAJDOWANIE PO H
        to_find = self.condition
        result = []
        cur.execute("SELECT nr_ki, rev, height FROM all_ki")
        for height in cur: 
            height
            if height[2] == int(to_find):
                result.append(height[0] + height[1])
        return (result)

    def find_customer(self):
    # ZNAJDOWANIE PO KLIENCIE
        to_find = self.condition
        result = []
        cur.execute("SELECT nr_ki, rev, customer FROM all_ki")
        for customer in cur: 
            customer
            if customer[2].lower() == to_find.lower(): 
                result.append(customer[0] + customer[1])
        return (result)

    def find_projectname(self):
    # ZNAJDOWANIE PO NAZWIE PROJEKTU
        to_find = self.condition
        result = []
        cur.execute("SELECT nr_ki, rev, project_name FROM all_ki")
        for name in cur: 
            name
            data = name[2].lower()
            data = data.find(to_find.lower())
            if data > -1: 
                result.append(name[0] + name[1])
        return (result)

    def find_rev(self):
        to_find = self.condition
        result = []
        cur.execute("SELECT nr_ki, rev, rev_status FROM all_ki")
        for ki in cur: 
            ki
            if to_find[:7] == ki[0]: 
                result.append(ki[0] + ' - rev: ' + ki[1] + ' - status: ' + ki[2])
        return (result)
    """
parametr = input("szukanie po: L, W, H, Kliencie, Nazwie projektu, Opisie, aktualna Rewizja: ")
szukana = input("szukana: ")
f = Search(szukana)
if parametr == 'L':
    print(f.find_lenght())
elif parametr == 'W':
    print(f.find_width())
elif parametr == 'H':
    print(f.find_height())
elif parametr == 'K':
    print(f.find_customer())
elif parametr == 'N':
    print(f.find_projectname())
elif parametr == 'O':
    print(f.find_phrase())
elif parametr == 'R':
    print(f.find_rev())
"""