# -*- coding: utf-8 -*-
from login import Logging, cs, cur
from searching import Search
import db_connect as db
import os
import socket
import pickle
import datetime 
import fpdf
from threading import Thread

def new_project():
    from project import Project
    #import webbrowser
    clientsocket.send(bytes("Czy chcesz utworzyć nowy projekt? [T/N]:", "UTF-8"))
    new_project = clientsocket.recv(1)
    if new_project.decode("utf-8") == 'T' or new_project.decode("utf-8") == 't':
        top_path = 'C:\\Firma\\DESIGNS\\'
        clientsocket.send(bytes("Klient:", "UTF-8"))
        customer = clientsocket.recv(64)
        customer = customer.decode("UTF-8")
        clientsocket.send(bytes("Nazwa projektu:", "UTF-8"))
        name_project = clientsocket.recv(128)
        name_project = name_project.decode("UTF-8")
        project = Project(top_path, customer.capitalize(), name_project.upper())
        project.new_project()
        nr_ki = project.last_num[:7]
        path_ = project.last_path + '\\' + project.last_num
        dat = datetime.datetime.now().date()
        tim = datetime.datetime.now().time()
        cur.execute("SELECT stat_name FROM status WHERE stat_id = 1")
        for record in cur:
            stat = record

        # OPIS PROJEKTU
        with open(path_ + '\\' + 'Opis.txt', 'w') as desc:
            clientsocket.send(bytes("Opis projektu:", "utf-8"))
            description = clientsocket.recv(4096)
            description = description.decode("utf-8")
            desc.write(description)

        # POBIERANIE NAZWISKA PROJEKTANTA
        """
        with open('C:\\Users\\Public\\Temp.json', 'r') as js:
            info = json.load(js)
            designer_name = info['f_name'] + " " + info['l_name']
            """

        # WSTAWIA NOWY PROJEKT DO TABELI all_ki
        clientsocket.send(bytes("name", "utf-8"))
        owner = clientsocket.recv(32)
        owner = owner.decode("utf-8")
        cur.execute("INSERT INTO all_ki (nr_ki, rev, rev_status, ki_path, customer, project_name, project_owner) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)", (nr_ki, 'A', stat, path_, customer, name_project, owner))

        # WSTAWIA DO TABELI hystory NOWY PROJEKT
        cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
            VALUES (%s, %s, %s, %s, %s)", (nr_ki, 'A', stat, dat, tim))

        # WYSŁANIE POTWIERDZENIA O UTWORZENIU PROJEKTU
        clientsocket.send(bytes("Utworzono nowy projekt: "+nr_ki+"A", "utf-8"))


    else:
        pass
    cs.commit()
    cs.close()

def update_approve():

    cs = db.Conn().conn()
    cur = cs.cursor()

    #Pobranie z BD numerów projektów z statusem WIP
    cur.execute("SELECT nr_ki, rev FROM all_ki WHERE rev_status = 'WIP'")

    proj = []
    for wip in cur:
        project = wip[0] + wip[1]
        proj.append(project)

    clientsocket.send(bytes("Projekty oczekujące na akceptację:", "UTF-8"))

    for p in proj: 
        clientsocket.send(bytes(p+"\n", "UTF-8"))

    nr_ki = clientsocket.send(bytes('Który numer KI akceptujesz?:', "utf-8"))
    nr_ki = clientsocket.recv(8)
    nr_ki = nr_ki.decode("utf-8")
    if nr_ki in proj:
        accept = clientsocket.send(bytes('Czy projekt jest ok? [T/N]:',"utf-8"))
        accept = clientsocket.recv(1)
        accept = accept.decode("utf-8")
        if accept.lower() == 't':
            nr = nr_ki[:7]
            rev = nr_ki[-1]
            # podaje status z BD
            cur.execute("SELECT stat_name FROM status WHERE stat_id = 2")
            for app in cur:
                approve = app[0]
            # aktualna data
            dat = datetime.datetime.now().date()
            # aktualny czas
            tim = datetime.datetime.now().time()
            # OPIS GABARYTÓW PROJEKTU
            clientsocket.send(bytes('Podaj gabaryty zewnętrzne produktu:', "utf-8"))
            l = clientsocket.send(bytes('L: ', "utf-8"))
            l = clientsocket.recv(16)
            l = l.decode("utf-8")
            w = clientsocket.send(bytes('W: ', "utf-8"))
            w = clientsocket.recv(16)
            w = w.decode("utf-8")
            h = clientsocket.send(bytes('H: ', "utf-8"))
            h = clientsocket.recv(16)
            h = h.decode("utf-8")
            # wstawianie do bazy do tabeli historycznej
            cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
                VALUES (%s, %s, %s, %s, %s)", (nr, rev, approve, dat, tim))        
            #wstawia do bazy gabaryty projektu
            cur.execute("UPDATE all_ki SET rev_status = %s, lenght = %s, width = %s, height = %s \
                WHERE nr_ki = %s AND rev = %s" , (approve, l, w, h, nr, rev))

            cur.execute("SELECT ki_path FROM all_ki WHERE nr_ki = %s" % ("'" + nr + "'"))
            for path in cur: 
                path = path[0]

            doc = fpdf.FPDF()
            doc.add_page()
            doc.set_font('Arial', '', 12)
            doc.cell(25, 10, nr_ki)
            doc.output(path+"\\"+nr+" rev "+rev+"\\"+nr_ki+"_doc.pdf", "F")

                    # WYSŁANIE POTWIERDZENIA O AKCEPTAACJI
            clientsocket.send(bytes("Projekt "+nr+rev+" został zaakceptowany.", "utf-8"))


        elif accept.lower() != 't':
            clientsocket.send(bytes("Brak akceptacji", "utf-8"))
    else: clientsocket.send(bytes("Nieprawidłowy numer KI", "utf-8"))
    cs.commit()
    cs.close()

def update_release():
    cs = db.Conn().conn()
    cur = cs.cursor()

    #Pobranie z BD numerów projektów z statusem APPROVED    
    clientsocket.send(bytes("Projekty oczekujące na uwolnienie do produkcji:"+"\n", "UTF-8"))

    cur.execute("SELECT nr_ki, rev FROM all_ki WHERE rev_status = 'APPROVED'")
    proj = []
    for app in cur:
        approved = app[0]+app[1]
        proj.append(approved)
        clientsocket.send(bytes(approved+'\n', "utf-8"))
        
    nr_ki = clientsocket.send(bytes('Który numer KI jest zwolniony do produkcji?:', "UTF-8"))
    nr_ki = clientsocket.recv(8)
    nr_ki = nr_ki.decode("utf-8")

    if nr_ki in proj:
        accept = clientsocket.send(bytes('Czy projekt jest ok? [T/N]:', "utf-8"))
        accept = clientsocket.recv(1)
        accept = accept.decode("utf-8")
        if accept == 't' or accept == 'T':
            dat = datetime.datetime.now().date()
            tim = datetime.datetime.now().time()
            nr = nr_ki[:7]
            rev = nr_ki[-1]

            # jeżeli rewizja projektu jest wyższa niż A to poprzednia dostaje status ARCHIVED
            if ord(rev) > 65 and ord(rev) < 91:
                prev_rev = chr(ord(rev)-1) # poprzednia litera od podanej

                # pobiera z BD status ARCHIVED
                cur.execute("SELECT stat_name FROM status WHERE stat_id = 4")
                for arch in cur:
                    arch = arch[0]
                # update numeru projektu do ARCHIVEED
                cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s AND rev = %s",\
                    (arch, nr, prev_rev))
                cs.commit()
                cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
                    VALUES (%s, %s, %s, %s, %s)", (nr, prev_rev, arch, dat, tim))
                cur.execute("DELETE FROM all_ki WHERE nr_ki = %s AND rev = %s AND rev_status = %s",\
                    (nr, prev_rev, arch))

            cur.execute("SELECT stat_name FROM status WHERE stat_id = 3")
            for rel in cur:
                rel = rel[0]
            cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s AND rev = %s",\
                (rel, nr, rev))
            cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
                VALUES (%s, %s, %s, %s, %s)", (nr, rev, rel, dat, tim))

            # wybiera ścieżke katalogu projektu
            cur.execute("SELECT ki_path FROM all_ki WHERE nr_ki = %s and rev = %s"\
                % ("'" + nr + "'", "'" + rev + "'"))
            for path in cur: path
            #podaje ścieżkę ostatniej rewizji produktu
            all_rev = os.listdir(path[0])
            for i in all_rev:
                if i[-1] == rev:
                    rev_path = path[0] + '\\' + i
            # tworzenie nowego pliku BOM dla reewizji
            bom_file = rev_path + '\\' + 'BOM.txt'
            file = open(bom_file, 'w')
            files = os.listdir(rev_path)
            for f in files:
                if f != 'BOM.txt' and f[0] != 'F' and f[-4:] == '.pdf' and f[-7:] != 'doc.pdf':
                    file.write(f[:-4] + '\n')
            file.close()

            clientsocket.send(bytes("""
            Dokument PDF utworzony.
            Projekt zwolniony do produkcji.
            ""","utf-8"))

        elif accept.lower() != 't':
            clientsocket.send(bytes("Brak akceptacji", "utf-8"))
    else: clientsocket.send(bytes("Nieprawidłowy numer KI", "utf-8"))
    cs.commit()
    cs.close()

def change_rev():
    cs = db.Conn().conn()
    cur = cs.cursor()
    nr_ki = clientsocket.send(bytes("Który numer projektu ma mieć podniesioną rewizję?", "utf-8"))
    nr_ki = clientsocket.recv(8)
    nr_ki = nr_ki.decode("utf-8")
    nr = nr_ki[:7]
    rev = nr_ki[-1]
    cur.execute("SELECT nr_ki, rev FROM all_ki WHERE nr_ki = %s AND rev_status = 'RELEASED' OR rev_status = 'APPROVED'"\
        % ("'"+nr+"'"))
    released = []
    for rel in cur:
        nr = rel[0]
        rev = rel[1]
        project = nr+rev
        released.append(project)
    if nr_ki in released:
            # podaje status WIP z BD
        cur.execute("SELECT stat_name FROM status WHERE stat_id = 1")
        for wip in cur:
            wip = wip[0]
        rev = ord(rev)
        if rev > 64 and rev < 91:
            rev += 1
            new_rev = chr(rev)
        else:
            print('Błąd. Za wysoka rewizja! Utwórz nowy projekt.')
            conn.close()
        # aktualna data
        dat = datetime.datetime.now().date()
        # aktualny czas
        tim = datetime.datetime.now().time()
        # wstawianie do bazy do tabeli historycznej
        cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
            VALUES (%s, %s, %s, %s, %s)", (nr, new_rev, wip, dat, tim))
        # pobiera dane z bazy - ścieżkę, klienta, nazwę
        cur.execute("SELECT ki_path, customer, project_name, project_owner FROM all_ki WHERE nr_ki = %s" % ("'" + nr + "'"))
        for kit in cur:
            path = kit[0]
            customer = kit[1]
            name_project = kit[2]
            project_owner = kit[3]
        # tworzenie nowego katalogu ścieżka do katalogu
        os.mkdir(path + '\\' + nr + ' rev ' + new_rev)
        # WSTAWIA PROJEKT z nowa rewizja DO TABELI all_ki z statusem wip
        cur.execute("INSERT INTO all_ki (nr_ki, rev, rev_status, ki_path, customer, project_name, project_owner) \
            VALUES (%s, %s, %s, %s, %s, %s, %s)", (nr, new_rev, wip, path, customer, name_project, project_owner))
        clientsocket.send(bytes("Utworzono nową rewizję ("+new_rev+") dla projektu "+nr,"utf-8"))
    else: clientsocket.send(bytes("Nieorawidłowy numer KI", "utf-8"))
    cs.commit()
    cs.close()

def archive():
    cs = db.Conn().conn()
    cur = cs.cursor()
    nr_ki = clientsocket.send(bytes("Który numer projektu wychodzi z produkcji?:", "utf-8"))
    nr_ki = clientsocket.recv(8)
    nr_ki = nr_ki.decode("utf-8")
    nr = nr_ki[:7]
    rev = nr_ki[-1]
    cur.execute("SELECT nr_ki, rev FROM all_ki WHERE nr_ki = %s AND rev_status = 'RELEASED'"\
    % ("'"+nr+"'"))
    released = []
    for rel in cur:
        nr = rel[0]
        rev = rel[1]
        project = nr+rev
        released.append(project)
    if nr_ki in released:
        # pobiera status ARCHIVED z bazy
        cur.execute("SELECT stat_name FROM status WHERE stat_id = 4")
        for arch in cur:
            arch = arch[0]

        # aktualna data
        dat = datetime.datetime.now().date()
        # aktualny czas
        tim = datetime.datetime.now().time()

        # wstawianie do bazy do tabeli historycznej
        cur.execute("INSERT INTO history (nr_ki, rev, stat, dat, tim) \
            VALUES (%s, %s, %s, %s, %s)", (nr, rev, arch, dat, tim))

        # aktualizuje status do ARCHIVED w podanym numerze KI
        cur.execute("UPDATE all_ki SET rev_status = %s WHERE nr_ki = %s AND rev = %s" , (arch, nr, rev))

        clientsocket.send(bytes("Projekt zarchiwizowany", "utf-8"))

    else: clientsocket.send(bytes("Nieorawidłowy numer KI", "utf-8"))
    cs.commit()
    cs.close()

def history():
    cs = db.Conn().conn()
    cur = cs.cursor()

    nr_ki = clientsocket.send(bytes("Numer projektu: ", "utf-8"))
    nr_ki = clientsocket.recv(8)
    nr_ki = nr_ki.decode("utf-8")

    cur.execute("SELECT dat, tim, nr_ki, rev, stat FROM history WHERE nr_ki = %s" % ("'"+nr_ki+"'"))
    clientsocket.send(bytes("Zmiany projektu "+nr_ki, "utf-8"))
    for i in cur:
        day = str(i[0].day)
        mon = str(i[0].month)
        yr = str(i[0].year)
        hr = str(i[1].hour)
        min = str(i[1].minute)
        sec = str(i[1].second)
        nr = i[2]
        rev = i[3]
        stat = i[4]
        history = nr+' - '+rev+' - '+stat+' - '+day+'-'+mon+'-'+yr+', '+hr+':'+min+':'+sec +"\n"
        clientsocket.send(bytes(history, "utf-8"))

def searching():
    search = ''
    while search.lower() != 'close':
        clientsocket.send(bytes("""
        Wyszukiwanie (Wpisz odpowiedni znak):
        - Opis ['O']: 
        - Długość ['L']: 
        - Szerokość ['W']: 
        - Wysokość ['H']:
        - Klient ['C']:
        - Nazwa Projektu ['N']: 
        - Sprawdź aktualną rewizję ['R']:
        lub 'close' aby zamknąć wyszukiwarkę.
        """, "utf-8"))
        search = clientsocket.recv(5)
        search = search.decode("utf-8")

        if search.lower() == 'o':
            clientsocket.send(bytes("Podaj szukaną frazę:","utf-8"))
            condition = clientsocket.recv(32)
            condition = condition.decode("utf-8")
            finder = Search(condition)
            print(finder.find_phrase())
            search = ''

        elif search.lower() == 'l':
            clientsocket.send(bytes("Podaj szukaną długość 'L'[mm]:","utf-8"))
            condition = clientsocket.recv(32)
            condition = condition.decode("utf-8")
            finder = Search(condition)
            clientsocket.send(bytes(finder.find_lenght(),"utf-8"))
            search = ''

        elif search.lower() == 'w':
            clientsocket.send(bytes("Podaj szukaną szerokość 'W'[mm]:","utf-8"))
            condition = clientsocket.recv(32)
            condition = condition.decode("utf-8")
            finder = Search(condition)
            finder.find_width()
            search = ''

        elif search.lower() == 'h':
            clientsocket.send(bytes("Podaj szukaną wyokość 'H'[mm]:","utf-8"))
            condition = clientsocket.recv(32)
            condition = condition.decode("utf-8")
            finder = Search(condition)
            finder.find_height()
            search = ''

        elif search.lower() == 'c':
            clientsocket.send(bytes("Podaj nazwę klienta:","utf-8"))
            condition = clientsocket.recv(32)
            condition = condition.decode("utf-8")
            finder = Search(condition)
            finder.find_customer()
            search = ''

        elif search.lower() == 'n':
            clientsocket.send(bytes("Podaj nazawę projektu:","utf-8"))
            condition = clientsocket.recv(32)
            condition = condition.decode("utf-8")
            finder = Search(condition)
            finder.find_projectname()
            search = ''

        elif search.lower() == 'r':
            clientsocket.send(bytes("Podaj numer projektu:","utf-8"))
            condition = clientsocket.recv(32)
            condition = condition.decode("utf-8")
            finder = Search(condition)
            finder.find_rev()
            search = ''

        else:
            "Wystąpił błąd!"

host = '192.168.13.6'
port = 34543
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
while True:     # start serwera
    s.listen(5) # Kolejkowanie max 5 żądań
    clientsocket , address = s.accept()
    ip, port = str(address[0]), str(address[1])
    print("Połączenie przychodzące z %s:%s", (ip, port))
    clientsocket.send(bytes("Witaj w Aplikacji.", "UTF-8"))
    Thread(target=client_thread, args=(clientsocket, ip, port)).start()
    # Logowanie
    log = False
    while log != True:
        login = clientsocket.send(bytes("Login: ", "UTF-8"))
        login = clientsocket.recv(32)
        login = login.decode("utf-8")
        passwd = clientsocket.send(bytes("Haslo: ", "UTF-8"))
        passwd = clientsocket.recv(32)
        passwd = passwd.decode("utf-8")
        loger = Logging(login, passwd)
        log = loger.logging()
        cur.execute("SELECT f_name, l_name, is_master FROM users WHERE login = %s" % ("'"+login+"'"))
        for info in cur: info
        info = {'f_name': info[0], 'l_name':info[1], 'master': info[2]}
        full_name = info['f_name'] + ' ' + info['l_name']
        #wysłanie informacji o zalogowanym do aplikacji klienta
        send_info = pickle.dumps(info)
        clientsocket.send(send_info)
    # Powitanie zalogowanego
    if log == True:
        welcome = "Witaj "+full_name
        clientsocket.send(bytes(welcome, "UTF-8"))
    # Opcje programu
    choice = ""
    while choice.lower() != "exit":
        clientsocket.send(bytes("""
        Wybierz co chcesz zrobić:
        - Utwórz nowy projekt [N]
        - Akceptuj projekt [A]
        - Uwolnij projekt do produkcji [R]
        - Podnieś rewizję [I]
        - Wycofaj z produkcji [W]
        - Wyszukaj projekt [F]
        - Sprawdź historię projektu [H]
        lub 'exit' aby zakończyć.
        """, "UTF-8"))

        choice = clientsocket.recv(32)
        choice = choice.decode("UTF-8")
        

        if choice.lower() == "n":
            new_project()
        elif choice.lower() == "a":
            clientsocket.send(bytes("master", "utf-8"))
            master = clientsocket.recv(8)
            master = master.decode("UTF-8")
            if master == 'True':
                update_approve()
            else: clientsocket.send(bytes("Nie masz uprawnień do tej funkcji.", "utf-8"))
        elif choice.lower() == "r":
            update_release()
        elif choice.lower() == "i":
            change_rev()
        elif choice.lower() == "f":
            searching()
        elif choice.lower() == 'h':
            history()
        elif choice.lower() == "w":
            archive()
        elif choice.lower() == "exit":
            clientsocket.send(bytes("Zakończono", "utf-8"))
            print(f"Zakończono połączenie z {address}")         # główna pętla programu


"""
def new():
    import socket
    import sys
    import traceback
    from threading import Thread
    def main():
       start_server()
    def start_server():
       host = "127.0.0.1"
       port = 8000 # arbitrary non-privileged port
       soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       print("Socket created")
       try:
          soc.bind((host, port))
       except:
          print("Bind failed. Error : " + str(sys.exc_info()))
          sys.exit()
       soc.listen(6) # queue up to 6 requests
       print("Socket now listening")
       # infinite loop- do not reset for every requests
       while True:
          connection, address = soc.accept()
          ip, port = str(address[0]), str(address[1])
          print("Connected with " + ip + ":" + port)
       try:
          Thread(target=client_thread, args=(connection, ip, port)).start()
       except:
          print("Thread did not start.")
          traceback.print_exc()
       soc.close()
    def clientThread(connection, ip, port, max_buffer_size = 5120):
       is_active = True
       while is_active:
          client_input = receive_input(connection, max_buffer_size)
          if "--QUIT--" in client_input:
             print("Client is requesting to quit")
             connection.close()
             print("Connection " + ip + ":" + port + " closed")
             is_active = False
          else:
             print("Processed result: {}".format(client_input))
             connection.sendall("-".encode("utf8"))
    def receive_input(connection, max_buffer_size):
       client_input = connection.recv(max_buffer_size)
       client_input_size = sys.getsizeof(client_input)
       if client_input_size > max_buffer_size:
          print("The input size is greater than expected {}".format(client_input_size))
       decoded_input = client_input.decode("utf8").rstrip()
       result = process_input(decoded_input)
       return result
    def process_input(input_str):
       print("Processing the input received from client")
       return "Hello " + str(input_str).upper()
    if __name__ == "__main__":
       main()
"""
