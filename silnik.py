import os
"""
gen = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
# Wskazanie głównego katalogu wyszukiwania - lista
main = os.listdir(gen)
fraza = input('Wpisz szukaną frazę: ')
fraza.lower()
for i in main:                  # Pętla przeszukująca katalog główny - przeszukuje katalogi z zakresami numerów projektów
    if i[0:2] == 'KI':          # jeżeli folder zaczyna się na "KI"...
        kat = os.listdir(gen + i)    # ... powstaje lista podkatalogów z numerami projektów
        for j in kat:           # pętla rozbierająca listę podkatalogów projektów
            #print(j)            # wydrukowanie numeru projektu
            kat2 = os.listdir(gen + i + '\\' + j + '\\')    # powstaje lista plików w folderze
            for k in kat2:      # pętla przeszukująca folder projektu
                if k[-4:] == '.txt':    # warunek jeżeli jest plik tekstowy, 
                    f = open(gen + i + '\\' + j + '\\' + k, 'r')     # plik jest otwierany w trybie odczytu
                    read_file = f.read()        # odczytanie pliku
                    f.close()                   # zamknięcie pliku
                    szukaj = read_file.find(fraza)  #przeszukiwanie pliku w celu znalezienia szukanej frazy
                    if szukaj > -1:             # Warunek wyszukiwania
                        print(j)                # Wyświetlanie numeru projektu ze znalezioną frazą
                        """

class Engine():
    def __init__(self, top):
        self.top = top
        
    def folder_search(self):
        intro = os.listdir(self.top)
        for i in intro:
            if i[0:2] == 'KI':
                print(i)
                des = os.listdir(self.top + i)
                for j in des:
                    print(j)

fraza = input("Podaj szukaną frazę: ")

kat_glowny = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
#katalogi = os.listdir(kat_glowny)

szukanie = Engine(kat_glowny)
szukanie.folder_search()
 



