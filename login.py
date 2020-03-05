import db_connect as db
cs = db.Conn().conn()
cur = cs.cursor()

class Logging:
    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd

    def logging(self):
        cur.execute("SELECT * FROM designers WHERE login = %s" % ("'" + self.login + "'"))
        for designer in cur: designer
        if designer[4] == self.login and self.passwd == designer[5]:
            return True

    def master(self):
        cur.execute("SELECT * FROM designers WHERE login = %s" % ("'" + self.login + "'"))
        for designer in cur: designer
        return designer[3]