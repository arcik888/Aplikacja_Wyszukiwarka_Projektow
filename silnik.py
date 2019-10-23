import os, webbrowser

class Engine():
    def __init__(self, top, phrase):
        self.top = top                  #podstawowa ścieżka do przezszukiwania
        self.phrase = phrase            #szukana fraza
        
    def folder_search(self):
        intro = os.listdir(self.top)    #lista katalogów do przeszukania
        for i in intro:                 #wejście w pętlę przeszukującą główny folder
            if i[0:2] == 'KI':          #warunek jeżeli katalog nazywa się "KI"
                des = os.listdir(self.top + i)  #tworzy się nowa lista katalogów
                for j in des:           #pętla przeszukująca niższy katalog 
                    fil = os.listdir(self.top + i + '\\' + j)   #tworzenie nowej listy katalogów niżej
                    for k in fil:       #pęta przeszukująca listę katalogów niższego rzędu
                        if k[-4:] == '.txt':    #jeżeli jest plik tekstowy
                            _path = self.top + i + '\\' + j + '\\'  #podana ścieżka do katalogu projektu
                            f = open(_path + k, 'r')    #otwarcie pliku tekstowego
                            read_file = f.read()        #przeczytanie pliku
                            f.close()                   #zamknięcie pliku
                            search = read_file.find(self.phrase)    #przeszukiwanie pliku żeby znaleźć szukaną frazę
                            if search > -1:             #jeżeli odczytana zawartość pliku zawiera szukaną frazę
                                print(j + " -> " + os.path.abspath(_path))  #wyświetlany jest numer projektu wraz ze ścuieżką dostępu
                                #webbrowser.open(_path) # otwiera okno folderu

                                """Trzeba zrobic w GUI przycisk, który b ędzie otwierał folder
                                    -> numer wyszukanego projektu
                                    -> ścieżka w systemie
                                    -> przycisk do otwarcia (Qbutton - otwiera folder zawierający
                                    """
                            


fraza = input("Podaj szukaną frazę: ")
kat_glowny = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
szukanie = Engine(kat_glowny, fraza)
szukanie.folder_search()
