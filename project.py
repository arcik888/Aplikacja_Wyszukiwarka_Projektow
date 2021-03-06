# Moduł dodaje nowy projekt do głównego katalogu parojektów
# -*- coding: utf-8 -*-

import os

class Project():
    def __init__(self, top, cust, name):
        self.top = top # główny katalog projektów
        self.cust = cust # nazwa klienta
        self.name = name # nazwa projektu

    def last_project(self):
        # Znajduje numer ostatniego projektu w katalogu
        self.top_cat = os.listdir(self.top)
        self.top_cat_KI = []

        for i in self.top_cat:
            if i[0:2] == 'KI':
                self.top_cat_KI.append(i)
        for j in self.top_cat_KI:
            if j[0:2] == 'KI':
                try:
                    self.des = os.listdir(self.top + j)
                except IndexError:
                    os.mkdir(self.top + j + '\\' + j[0:7])
                    self.des = os.listdir(self.top + j)
        for k in self.des:
            if k[0:2] == 'KI':
                try:
                    self.des2 = os.listdir(self.top + j + '\\' + k)
                    self.last_num = self.des2[-1]
                except IndexError:
                    self.last_num = os.mkdir(self.top + j + '\\' + k + '\\' + k[0:7] + ' - ' + \
                                             self.cust + ' - ' + self.name)
                    self.des2 = os.listdir(self.top + j + '\\' + k)
       
        return self.top_cat_KI, self.des, self.des2, self.last_num

    def new_project(self):
        """
        Metoda tworzy nowy katalog dla projektu i pierwszą - rewizję projektu.
        Jeżeli ostatni numer projektu jest ostatnim z zakresu, 
        tworzony jest nowy folder z wyższym zakresem.
        """

        def create_top_cat(self):
            self.new_top_cat = 'KI' + str(int(Project.last_project(self)[3][2:7]) + 1) + \
                ' - KI' + str(int(Project.last_project(self)[3][2:7]) + 1000)
            self.new_path = self.top
            os.mkdir(self.top + '\\' + self.new_top_cat)

        def create_mid_cat(self):
            self.new_mid_cat = 'KI' + str(int(Project.last_project(self)[3][2:7]) + 1) + \
               ' - KI' + str(int(Project.last_project(self)[3][2:7]) + 100)
            self.new_path = self.top + Project.last_project(self)[0][-1]
            os.mkdir(self.top + Project.last_project(self)[0][-1] + '\\' + self.new_mid_cat)

        def create_low_cat(self):
            self.new_num = 'KI' + str(int(Project.last_project(self)[3][2:7]) + 1)
            self.new_path = self.top + Project.last_project(self)[0][-1] + '\\' + \
               Project.last_project(self)[1][-1]
            os.mkdir(self.new_path + '\\' + self.new_num + ' - ' + self.cust + ' - ' + self.name)

        def create_rev_cat(self):
            self.new_path = self.top + Project.last_project(self)[0][-1] + '\\' + \
               Project.last_project(self)[1][-1]
            os.mkdir(self.new_path + '\\' + Project.last_project(self)[3] + '\\' + \
                Project.last_project(self)[3][0:7] + ' rev A')
            self.last_path = self.top + Project.last_project(self)[0][-1] + '\\' + \
                Project.last_project(self)[1][-1]

        if Project.last_project(self)[2][-1][0:7] == Project.last_project(self)[0][-1][-7:]:
            create_top_cat(self)
            create_mid_cat(self)
            create_rev_cat(self)

        elif Project.last_project(self)[2][-1][0:7] == Project.last_project(self)[1][-1][-7:]:
            create_mid_cat(self)
            create_rev_cat(self)
            
        else:
            create_low_cat(self)
            create_rev_cat(self)
