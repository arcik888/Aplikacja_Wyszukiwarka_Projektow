# Moduł dodaje nowy projekt do głównego katalogu parojektów
import os

class Project():
    def __init__(self, top, new):
        self.top = top
        self.new = new

    def new_project(self):
        # Znajduje ostatni numer projektu w katalogu głównym
        cust = input("Klient: ")
        name = input('Nazwa projektu: ')

        top_cat = os.listdir(self.top)
        for i in top_cat:
            if i[0:2] == 'KI':
                self.des = os.listdir(self.top + i + '\\')
                for j in self.des:
                    if j[0:2] == 'KI':
                        self.des2 = os.listdir(self.top + i + '\\' + j + '\\')
                        self.last_num = self.des2[-1][2:7]

                        if 'KI' + str(self.last_num) == self.des[-1][-7:]:
                            mid_cat = 'KI' + str(int(self.last_num) + 1) + ' - KI' + str(int(self.last_num) + 100)
                            os.mkdir(self.top + i + '\\' + mid_cat)
                            self.new_num = 'KI' + str(int(self.last_num) + 1)
                            self.new_path = self.top + i + '\\' + mid_cat + '\\' + self.new_num
                            os.mkdir((self.top + i + '\\' + mid_cat + '\\' + self.new_num) + ' - ' + cust + ' - ' + name)

                        else:
                            self.new_num = 'KI' + str(int(self.last_num) + 1)
                            self.new_path = self.top + i + '\\' + j + '\\' + self.new_num
                            os.mkdir(self.new_path + ' - ' + cust + ' - ' + name)
            #os.mkdir(self.new_path + ' - ' + cust + ' - ' + name)
        print("Utworzono katalog nowego projektu: " + self.new_path)

top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
new_project = input("Czy chcesz utworzyć nowy projekt? [T/N]: ")

project = Project(top_path, new_project)
project = Project(top_path, new_project)

if project.new == 'T' or project.new == 't':
    project.new_project()
else:
    pass