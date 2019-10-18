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

class Silnik():
    def __init__(self, gen, top):
        #self.fraza = fraza
        #self.gen = gen
        #self.main = main
        self.gen = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'
        self.top = os.listdir(self.gen)

    def wyszukiwanie(self):
        for i in self.top:
            print(i)


fraza = input("Podaj szukaną frazę: ")
szukanie = Silnik.wyszukiwanie(fraza)


