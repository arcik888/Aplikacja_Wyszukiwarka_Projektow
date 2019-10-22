import os

class Engine():
    def __init__(self, top, phrase):
        self.top = top
        self.phrase = phrase
        
    def folder_search(self):
        intro = os.listdir(self.top)
        for i in intro:
            if i[0:2] == 'KI':
                des = os.listdir(self.top + i)
                for j in des:
                    fil = os.listdir(self.top + i + '\\' + j)
                    for k in fil:
                        if k[-4:] == '.txt':
                            path = self.top + i + '\\' + j + '\\'
                            f = open(path + k, 'r')
                            read_file = f.read()
                            f.close()
                            search = read_file.find(self.phrase)
                            if search > -1: 
                                print(j + " -> " + os.path.abspath(path))
                                #print(os.path.abspath(path))
                            


fraza = input("Podaj szukaną frazę: ")
kat_glowny = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
szukanie = Engine(kat_glowny, fraza)
szukanie.folder_search()
