import os
import new_project

top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
new = input("Czy chcesz utworzyć nowy projekt? [T/N]: ")
customer = input("Klient: ")
name_project = input('Nazwa projektu: ')

project = new_project.Project(top_path, customer, name_project)

if new == 'T' or new == 't':
    project.new_project()
else:
    pass

#os.mkdir(project.top_path + "new rev")v 
