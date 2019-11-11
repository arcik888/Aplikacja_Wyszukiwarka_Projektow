# Moduł dodaje nowy projekt do głównego katalogu parojektów
import os

class Project():
    def __init__(self, top, cust, name):
        self.top = top
        self.cust = cust
        self.name = name

    #def last_project(self):
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
                    self.last_num = os.mkdir(self.top + j + '\\' + k + '\\' + k[0:7] + ' - ' + self.cust + ' - ' + self.name)
                    self.des2 = os.listdir(self.top + j + '\\' + k)
       
        #return self.top_cat_KI, self.des, self.des2, self.last_num

    def new_project(self):
        """
        Metoda tworzy nowy katalog dla projektu i pierwszą - rewizję projektu.
        Jeżeli ostatni numer projektu jest ostatnim z zakresu, 
        tworzony jest nowy folder z wyższym zakresem.
        """
        def create_top_cat(self):
            self.new_top_cat = 'KI' + str(int(self.last_num[2:7]) + 1) + ' - KI' + str(int(self.last_num[2:7]) + 1000)
            self.new_path = self.top
            os.mkdir(self.top + '\\' + self.new_top_cat)

        def create_mid_cat(self):
            self.new_mid_cat = 'KI' + str(int(self.last_num[2:7]) + 1) + ' - KI' + str(int(self.last_num[2:7]) + 100)
            self.new_path = self.top + self.top_cat_KI[-1]
            os.mkdir(self.top + Project.last_project(self)[0][-1] + '\\' + self.new_mid_cat)

        def create_low_cat(self):
            self.new_num = 'KI' + str(int(self.last_num[2:7]) + 1)
            self.new_path = self.top + self.top_cat_KI[-1] + '\\' + self.des[-1]
            os.mkdir(self.new_path + '\\' + self.new_num + ' - ' + self.cust + ' - ' + self.name)

        def create_rev_cat(self):
            self.new_path = self.top + self.top_cat_KI[-1] + '\\' + self.des[-1] + '\\' + self.last_num
            os.mkdir(self.new_path + '\\' + self.last_num[0:7] + ' rev A')
            self.last_path = self.new_path + '\\' + self.last_num[0:7]

        if self.des2[-1][0:7] == self.top_cat_KI[-1][-7:]:
            create_top_cat(self)
            create_mid_cat(self)
            create_rev_cat(self)

        elif self.des2[-1][0:7] == self.des[-1][-7:]:
            create_mid_cat(self)
            create_rev_cat(self)
            
        else:
            create_low_cat(self)
            create_rev_cat(self)

        print("Utworzono katalog nowego projektu: " + self.last_path)

    def description(self):
        desc_file = open(Opis + self.last_num, 'w')
        desc_file.write()

        """
top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'


new_project = input("Czy chcesz utworzyć nowy projekt? [T/N]: ")
customer = input("Klient: ")
name_project = input('Nazwa projektu: ')
project = Project(top_path, customer, name_project)


if new_project == 'T' or new_project == 't':
    project.new_project()
else:
    pass
"""