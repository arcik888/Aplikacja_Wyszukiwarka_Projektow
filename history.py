import db_connect as db
import datetime as dt

cs = db.Conn().conn()
cur = cs.cursor()

nr_ki = input("Numer projektu: ")

cur.execute("SELECT * FROM history WHERE nr_ki = %s" % ("'"+nr_ki+"'"))
print("Zmiany projektu "+nr_ki)
for i in cur:
    day = str(i[4].day)
    mon = str(i[4].month)
    yr = str(i[4].year)
    hr = str(i[5].hour)
    min = str(i[5].minute)
    sec = str(i[5].second)
    nr = i[1]
    rev = i[2]
    stat = i[3]
    print(nr+' - '+rev+' - '+stat+' - '+day+'-'+mon+'-'+yr+', '+hr+':'+min+':'+sec)
