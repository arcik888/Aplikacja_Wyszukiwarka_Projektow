import os

# Wskazanie głównego katalogu wyszukiwania - lista
main = os.listdir('C:\\Users\\arcik\\Desktop\\DESIGNS')
fraza = input('Wpisz szukaną frazę: ')
for i in main:                  # Pętla przeszukująca katalog główny - przeszukuje katalogi z zakresami numerów projektów
    if i[0:2] == 'KI':          # jeżeli folder zaczyna się na "KI"...
        kat = os.listdir('C:\\Users\\arcik\\Desktop\\DESIGNS\\' + i)    # ... powstaje lista podkatalogów z numerami projektów
        for j in kat:           # pętla rozbierająca listę podkatalogów projektów
            #print(j)            # wydrukowanie numeru projektu
            kat2 = os.listdir('C:\\Users\\arcik\\Desktop\\DESIGNS\\' + i + '\\' + j)    # powstaje lista plików w folderze
            for k in kat2:      # pętla przeszukująca folder projektu
                if k[-4:] == '.txt':    # warunek jeżeli jest plik tekstowy, 
                    f = open('C:\\Users\\arcik\\Desktop\\DESIGNS\\' + i + '\\' + j + '\\' + k, 'r')     # plik jest otwierany w trybie odczytu
                    read_file = f.read()        # odczytanie pliku
                    f.close()                   # zamknięcie pliku
                    szukaj = read_file.find(fraza)  #przeszukiwanie pliku w celu znalezienia szukanej frazy
                    if szukaj > -1:             # Warunek wyszukiwania
                        print(k)                # Wyświetlanie numeru projektu ze znalezioną frazą