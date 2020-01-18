l = input("Podaj długość [mm]: ")
w = input("Podaj szerokość [mm]: ")
h = input("Podaj grubość [mm]: ")
a = input("Czy antystatyczna? [T/N]: ")
if a.lower() == 'n':
    c = input("Kolor [W/B]: ")
d = input("Gęstość [22/24/27/35/65/100]: ")
r = input("Jaki % recyklingu? [10/50]: ")
t = input("Piana PE czy PU? ")
s = input("Ze skórką? [T/N] ")

def wb():
    if a.lower() == 't':
        return 'P'
    elif c.lower() == 'w':
        return 'W'
    elif c.lower() == 'b':
        return 'B'

def color():
    if wb() == 'P':
        return 'Antystatyczna Różowa, '
    elif wb() == 'W':
        return 'Biała, '
    elif wb() == 'B':
        return 'Czarna, '

def density():
    if int(d) == 22:
        return 'F'
    elif int(d) == 24:
        return 'L'
    elif int(d) == 27:
        return 'S'
    elif int(d) == 35:
        return 'M'
    elif int(d) == 65:
        return 'H'
    elif int(d) == 100:
        return 'U'

def skin():
    if s.lower() == 't':
        return 'L'
    elif s.lower() == 'n':
        return '0'

def rec():
    return r + "% recyklingu, "

def skin_d(): 
    if skin() == 'L':
        return "ze skórką"
    else:
        return ""

L = l[:2]
W = w[:2]
H = h[:2]
C = wb()
D = density()
R = r[0]
T = t[1]
S = skin()

code = D + C + T + L + W + H + R + S

print(code)

description = "Piana " + t + ", " + d + "kg/m^3, " + l + "x" + w + "x" + h + "mm, " + color() + rec() + skin_d()

print(description)