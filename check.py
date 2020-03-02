def check():
# sprawdzenie czy podany numer KI jest prawidłowy i czy występuje taki w bazie
    if len(nr_ki) == 8:
        prefix = nr_ki[0:2]
        number = nr_ki[2:7]
        revision = nr_ki[7]

        if prefix.upper() == 'KI':
            pr = True
        elif prefix.upper() != 'KI':
            pr = False


        nr_kit = prefix + number
        cur.execute("SELECT nr_ki FROM all_ki WHERE nr_ki = %s" % ("'" + nr_kit + "'"))
        for nr in cur: 
            if nr in cur:
                number = nr[2:7]
            else: 
                nr = False
        try: 
            int(number)
            nr = True
        except TypeError:
            nr = False

        cur.execute("SELECT rev FROM all_ki WHERE nr_ki = %s" % ("'" + nr_kit + "'"))
        for rev in cur: rev
        if revision in rev: 
            rv = True
        else: 
            rv = False

        if pr == True and nr == True and rv == True:
            return True
        else:
            return False
    else:
        return False

