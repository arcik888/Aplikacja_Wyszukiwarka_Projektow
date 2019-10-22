import silnik

fraza = input("Podaj szukaną frazę: ")

kat_glowny = 'C:\\Users\\arcik\\Desktop\\DESIGNS\\'

szukanie = silnik.Engine(kat_glowny, fraza)
szukanie.folder_search()
