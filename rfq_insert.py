
seller = '' # wprowadzający zapytanie do systemu
        
log = False
while log != True:
    login = input("Login: ")
    passwd = getpass.getpass("Hasło: ")
    loger = Logging(login, passwd)
    log = loger.logging()

    cur.execute("SELECT * FROM users WHERE login = %s" % ("'"+login+"'"))
    for info in cur: info
    info = {'f_name': info[1], 'l_name':info[2], 'master': info[3]}
    with open('C:\\Users\\Public\\Temp.json', 'w') as js:
        json.dump(info, js)

designer = '' # nadawany w momencie przeyjęcia zlecenia rfq
priority = 2 # priorytet 2 z automatu - jeżeli wyższy, zmienić pozniej
date_rfq = datetime.datetime.now().date() # pobrać aktualną datę
reply_date = datetime.datetime.now().date() # pobrać aktualną datę
rfq_status = 'WAITING' # pobrać z bazy danych - nadanie pierwszego statusu z automatu

# jak będą zapytania oczekujące na przyjęcie - niech wyświetla się komunikat.

#SELECT rfq_year, rfq_num, customer, rfq_name, seller, designer, priority, date_rfq, reply, rfq_status FROM public.rfq_mgmt;
#       year      rfq_num   customer name      z bd     z bd      zmienna   dt        dt     zmienna
