import os
from project import Project
import psycopg2 as pg

top_path = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'

project = Project(top_path, 'Syncreon', 'KI32938')

print(project.last_project()[3])

f = project.top.find(project.name)
print(f)

#os.mkdir(project.last_project()[3][:7] + '\\' + project.last_project()[3][:7] + "new rev")

