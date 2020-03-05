import psycopg2 as pg
class Conn:
    def __init__(self, dbname='projects', user='postgres', password='Pa$$w0rd'):
        self.dbname = dbname
        self.user = user
        self.password = password

    def conn(self):
        self.connect = pg.connect(dbname = self.dbname, user = self.user, password = self.password)
        return self.connect




