import json

num = "Numer projektu"
name = "Nazwa projektu"
customer = "Nazwa Klienta"
desc = "Opis projektu"
clas = "Klasyfikacja projektu"
large = "krotka z wymiarami projektu"
mat = "Uzyty material"
gat = "Gatunek materialu"

file = {'Numer':num, 'Nazwa':name, 'Klient':customer, 'Opis':desc, 'Klasa':clas, 'Gabaryty':large, 'Material':mat, 'gatunek':gat}

with open(num+'.json', 'w') as json_file:
    json.dump(file, json_file)

"""- Nazwa projektu
- Numer projektu
- Klient
- Opis słowny projektu
- Gabaryty projektu
- Klasyfikacja materiałów (karton, piana, mix)
- rodzaj materiału (gęstość, gramatura)
- inne
"""