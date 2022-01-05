import sqlite3


class Statistic:
    def __init__(self):
        self.con = sqlite3.connect('leaders')
        self.conn = None
        try:
            self.conn = sqlite3.connect('leaders')
            print(sqlite3.version)
        except Exception as e:
            print(e)

    def create_db(self):
        pass

    def get_leaders(self, count=10):
        pass

    def save_sassion(self, name, score, table):
        pass

    def load_sassion(self):
        pass
